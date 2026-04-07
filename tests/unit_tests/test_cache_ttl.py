import hashlib
import os
import pathlib
import tempfile
import time
import unittest.mock

import pytest
import requests

from casanovo import casanovo
from casanovo.casanovo import CACHE_TTL_SECONDS


def test_get_weights_from_url_fresh_cache(monkeypatch):
    """
    Fresh cache (within TTL) should skip the network entirely.
    No HEAD or GET requests should be made when cache is still valid.
    """
    file_url = "http://example.com/model_weights.ckpt"

    with tempfile.TemporaryDirectory() as tmp_dir:
        cache_dir = pathlib.Path(tmp_dir)

        # Mock network calls - these should NOT be triggered for fresh cache
        mock_get = unittest.mock.MagicMock()
        mock_head = unittest.mock.MagicMock()
        monkeypatch.setattr(requests, "get", mock_get)
        monkeypatch.setattr(requests, "head", mock_head)

        # Create a fake cached weights file
        url_hash = hashlib.shake_256(file_url.encode("utf-8")).hexdigest(5)
        cache_file_dir = cache_dir / url_hash
        cache_file_dir.mkdir(parents=True)
        cache_file = cache_file_dir / "model_weights.ckpt"
        cache_file.write_bytes(b"fake weights")

        # Set mtime to half the TTL ago so cache is still fresh
        recent_time = time.time() - (CACHE_TTL_SECONDS / 2)
        os.utime(cache_file, (recent_time, recent_time))

        # Should return cached file without any network calls
        result = casanovo._get_weights_from_url(file_url, cache_dir)

        # Verify correct file returned and no network calls were made
        assert result.resolve() == cache_file.resolve()
        mock_head.assert_not_called()
        mock_get.assert_not_called()

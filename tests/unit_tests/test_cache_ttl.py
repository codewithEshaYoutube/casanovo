import hashlib
import os
import pathlib
import tempfile
import time
import unittest.mock

import pytest
import requests

from casanovo import casanovo


def test_get_weights_from_url_fresh_cache(monkeypatch):
    """Fresh cache should skip the network entirely."""
    file_url = "http://example.com/model_weights.ckpt"

    with tempfile.TemporaryDirectory() as tmp_dir:
        cache_dir = pathlib.Path(tmp_dir)

        mock_get = unittest.mock.MagicMock()
        mock_head = unittest.mock.MagicMock()
        monkeypatch.setattr(requests, "get", mock_get)
        monkeypatch.setattr(requests, "head", mock_head)

        # Create a fake cached file
        url_hash = hashlib.shake_256(file_url.encode("utf-8")).hexdigest(5)
        cache_file_dir = cache_dir / url_hash
        cache_file_dir.mkdir(parents=True)
        cache_file = cache_file_dir / "model_weights.ckpt"
        cache_file.write_bytes(b"fake weights")

        # Set mtime to 1 minute ago (fresh, within TTL)
        recent_time = time.time() - 60
        os.utime(cache_file, (recent_time, recent_time))

        result = casanovo._get_weights_from_url(file_url, cache_dir)

        assert result.resolve() == cache_file.resolve()
        mock_head.assert_not_called()
        mock_get.assert_not_called()


def test_get_weights_from_url_fresh_cache(tmp_path, monkeypatch):
    """Fresh cache within TTL should return cached path without any network call."""
    import time
    from unittest.mock import patch
    from casanovo import casanovo as casanovo_mod
    import hashlib, urllib.parse

    file_url = "https://example.com/model.ckpt"

    cache_file_name = "model.ckpt"
    url_hash = hashlib.shake_256(file_url.encode("utf-8")).hexdigest(5)
    cache_file_dir = tmp_path / url_hash
    cache_file_dir.mkdir(parents=True)
    cache_file_path = cache_file_dir / cache_file_name
    cache_file_path.write_text("fake weights")

    now = time.time()
    os.utime(cache_file_path, (now, now))

    with patch("casanovo.casanovo.requests.head") as mock_head:
        result = casanovo_mod._get_weights_from_url(file_url, tmp_path)

        assert result == cache_file_path
        mock_head.assert_not_called()

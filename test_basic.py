import grimreaper


def test_initializing():
    gr = grimreaper.GrimReaper(socket_path='foo', process_timeout=3)
    assert gr._path == 'foo'
    assert gr._process_timeout == 3

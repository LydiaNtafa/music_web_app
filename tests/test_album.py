from lib.album import Album

def test_format():
    album = Album(1, "My title", 2023, 1)
    assert album.id == 1
    assert album.title == "My title"
    assert album.release_year == 2023
    assert album.artist_id == 1

def test_display():
    album = Album(1, "My title", 2023, 1)
    assert str(album) == "Album(1, My title, 2023, 1)"
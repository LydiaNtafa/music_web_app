from lib.album_repository import *
from lib.album import *

'''
Test adding a new album and that reflecting in the all() result set 
'''
def test_create_album(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repo = Album_repository(db_connection)
    album = Album(None, "Blank Space", 2014, 2)
    repo.create(album)
    assert repo.all() == [
    Album(1, "After hours", 2020, 1),
    Album(2, "Blank Space", 2014, 2)]
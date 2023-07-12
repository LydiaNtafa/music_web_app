from lib.album import *


class Album_repository():
    
    def __init__(self, connection):
        self.connection = connection

    def create(self,album):
        self.connection.execute("INSERT INTO albums(title, release_year, artist_id) VALUES (%s, %s, %s)",
                                [album.title,album.release_year, album.artist_id])
        
    def all(self):
        rows = self.connection.execute("SELECT * FROM albums")
        album_list = []
        for row in rows:
            album = Album(row["id"], row["title"], row["release_year"],row["artist_id"])
            album_list.append(album)
        return album_list
from lib.artist import Artist

class ArtistRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        list_of_artist = []
        rows = self.connection.execute("SELECT * FROM artists")
        for row in rows:
            artist = Artist(row["id"], row["name"], row["genre"])
            list_of_artist.append(artist)
        return list_of_artist

    def add(self, artist):
        self.connection.execute("INSERT INTO artists(name, genre) VALUES (%s, %s)", [artist.name, artist.genre])
        return ""
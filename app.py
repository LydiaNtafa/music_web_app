import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import *
from lib.album import *

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/albums', methods = ['POST'])
def post_album():
    connection = get_flask_database_connection(app)
    repository = Album_repository(connection)
    if 'title' not in request.form:
        return "Need more information !", 400

    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']   
    album = Album(None, title,release_year, artist_id)
    repository.create(album)
    return ""

#its default anyway,
@app.route('/albums', methods = ['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = Album_repository(connection)
    list_of_album = repository.all()
    print(list_of_album)
    response = ""
    for album in list_of_album:
        response += f"{album}\n"
    return response



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))


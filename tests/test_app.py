# Tests for your routes go here

# Scenario 1
# -- 
#  POST/ albums
#  title: Dawn FM
#  release_year: 2022
#  artist_id: 1
# Expected response: 200 OK
# """
# """(no content)
#  GET/ albums
#  Expected response: 200 OK
#  """
#  Album(1,'After hours', 2020 , 1)
#  Album(2, 'Dawn FM' , ,2022 , 1)
def test_post_albums(web_client,db_connection):
    db_connection.seed('seeds/record_store.sql')
    response = web_client.post('/albums',data = {
        'title' :'Dawn FM',
        'release_year' : '2022',
        'artist_id' : '1'
    })
    assert response.status_code == 200
    # assert response.data.decode('utf-8') == ""
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
    "Album(1, After hours, 2020, 1)\n"\
    "Album(2, Dawn FM, 2022, 1)\n"

# Scenario 2
#  POST/ albums
#  title: 
#  release_year: 
#  artist_id: 
# Expected response: 400 Bad request
# """
# Need more information !
# """
def test_post_albums_error(web_client,db_connection):
    db_connection.seed('seeds/record_store.sql')
    response = web_client.post('/albums')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "Need more information !"

# Scenario 3
#  --
#  GET/artists
#  Parameters: none
#  Expected Reponse: 200 ok
#  ""
#  Pixies, ABBA, Taylor Swift, Nina Simone
def test_get_artists(web_client, db_connection):
    db_connection.seed('seeds/record_store.sql')
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone"


#  Scenario 4
#  --
# POST /artists
# Parameters:
# name=Wild nothing
# genre=Indie
# Expected response (200 OK)
# (No content)
# GET /artists
# Expected response (200 OK)
# Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing

def test_post_artist(web_client,db_connection):
    db_connection.seed('seeds/record_store.sql')
    response = web_client.post('/artists', data = {
        'name':'Wild Nothing',
        'genre': 'Indie'
    })
    assert response.status_code == 200
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone, Wild Nothing"

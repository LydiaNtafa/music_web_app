1. Design the Route Signature
Include the HTTP method, the path, and any query or body parameters.

--test-drive a route POST /albums to create a new album:




# albums route
'''
POST /albums
  title: str
  release_year: number(str)
  artist_id: number (str)

GET /albums
'''

2. Create Examples as Tests
Go through each route and write down one or more example responses.

Remember to try out different parameter values.

Include the status code and the response body.

Scenario 1
-- 
 POST/ albums
 title: Dawn FM
 release_year: 2022
 artist_id: 1
Expected response: 200 OK
"""
"""(no content)
--

 GET/ albums
 Expected response: 200 OK
 """
 Album(1,'After hours', 2020 , 1)
 Album(2, 'Dawn FM' , ,2022 , 1)



Scenario 2
--
 POST/ albums
 title: 
 release_year: 
 artist_id: 
Expected response: 400 Bad request
"""
Need more information !
"""

 GET/ albums
 Expected response: 200 OK
 """
 Album(1,'After hours', 2020 , 1)


""" everything send via request is STR"""

# EXAMPLE

# GET /home
#  Expected response (200 OK):
"""
This is my home page!
"""

# GET /wave?name=Leo
#  Expected response (200 OK):
"""
I am waving at Leo
"""

# GET /wave
#  Expected response (200 OK):
"""
I am waving at no one!
"""

# POST /submit
#  Parameters:
#    name: Leo
#    message: Hello world
#  Expected response (200 OK):
"""
Thanks Leo, you sent this message: "Hello world"
"""

# POST /submit
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Please provide a name and a message
"""
3. Test-drive the Route
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
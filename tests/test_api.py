"""
API tests using requests and pytest.
Tests include GET, POST, PUT, DELETE requests.
"""
import responses
import requests

def test_get_users():
    """Test that the users endpoint returns a list of users with status 200."""
    response = requests.get("https://jsonplaceholder.typicode.com/users", timeout=10)
    assert response.status_code == 200

    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0
    assert "name" in users[0]

def test_create_post():
    """Test creating a new post via the posts endpoint."""
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(url, json=payload, timeout=10)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "foo"
    assert data["body"] == "bar"
    assert data["userId"] == 1

def test_update_post():
    """Test updating a post using PUT request."""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    payload = {
        "id": 1,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }
    response = requests.put(url, json=payload, timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "updated title"
    assert data["body"] == "updated body"

def test_delete_post():
    """Test deleting a post using DELETE request."""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.delete(url, timeout=10)
    assert response.status_code == 200

def test_get_with_auth():
    """Test GET request with Authorization header."""
    url = "https://jsonplaceholder.typicode.com/posts"
    headers = {
        "Authorization": "Bearer fake_token_123"
    }
    response = requests.get(url, headers=headers, timeout=10)
    assert response.status_code == 200

@responses.activate
def test_mocked_get():
    """Test GET request with mocked response."""
    test_url = "https://api.example.com/data"
    responses.add(
        responses.GET,
        test_url,
        json={"key": "value"},
        status=200
    )

    response = requests.get(test_url, timeout=10)

    assert response.status_code == 200
    data = response.json()
    assert data["key"] == "value"

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_user_returns_200():
    # ARRANGE + ACT: send a GET request for user 1
    response = requests.get(f"{BASE_URL}/users/1")

    # ASSERT: Check the status code is OK
    assert response.status_code == 200

def test_get_user_has_correct_data():
    response = requests.get(f"{BASE_URL}/users/1")

    # parse the JSON body into a Python Dict
    data = response.json()

    # ASSERT: User 1's id should be 1
    assert data["id"] == 1
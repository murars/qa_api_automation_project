import pytest
from utils.api_client import APIClient
import uuid


@pytest.fixture(scope = 'module')
def api_clint():
    return APIClient()

def test_get_user(api_clint):
    response = api_clint.get('users')
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0
    
def test_create_user(api_clint, load_user_data):
    # user_data ={
    #     "name" : "Jhon",
    #     "user" : "QA Lead", 
    #     "email" : "jDoea@gmail"       
    # }
    user_data = load_user_data["new_user"]
    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
    print(unique_email)
    user_data["email"] = unique_email
    response = api_clint.post("users",user_data)
    print(response.json())
    assert response.status_code == 201 
    assert response.json()['name'] == 'Ricco'
    id = response.json()['id']
    responseget = api_clint.get('users/10')
    print(responseget.json())
    assert responseget.status_code == 200
    assert responseget.json()['name'] == 'Clementina DuBuque'
    
def test_update_user(api_clint):
    user_data ={
        "name" : "Jhon D",
        "user" : "QA Lead", 
        "email" : "jDoea@gmail"       
    }
    response = api_clint.put('users/1',user_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['name'] == 'Jhon D'

def test_delete_user(api_clint):
    response = api_clint.delete("users/1")
    print(response.json())
    assert response.status_code == 200
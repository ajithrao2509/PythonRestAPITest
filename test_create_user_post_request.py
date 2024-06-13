import random


import pytest
import requests
from Utilities.read_csv_data import read_test_data_from_csv

endpoint = "https://gorest.co.in/public/v2/users/"


# testing web_app used = https://gorest.co.in/


@pytest.mark.parametrize("name, email, gender, status", read_test_data_from_csv())
def test_post_rqst(name, email, gender, status):
    # create user
    print("post rqst")
    print(name)
    payload = {"name": name, "email": email, "gender": gender, "status": status}
    headers = {
        "content-type": "application/json",
        "Authorization": "Bearer e3560753d7d995ff245c508465a595a9907965067a7d88a452477ac532d74d7f",
    }
    response = requests.post(endpoint, json=payload, headers=headers)
    print(response.status_code)
    assert response.status_code == 422
    data = response.json()
    print(data)
    global id_user
    id_user = random.randint(25000, 50000)
    print(id_user)


def test_get_rqst():
    # get user
    print("get rqst")
    headers = {
        "content-type": "application/json",
        "Authorization": "Bearer 7b614933cf817fa46a516d23a3cb2b7ff514426adbe4e9edd2f40346d622eb26",
    }
    response = requests.get(endpoint + f"{id_user}", headers=headers)
    print(response.status_code)
    print(response.json())


def test_put_rqst():
    # update user
    print("put rqst")
    headers = {
        "content-type": "application/json",
        "Authorization": "Bearer 7b614933cf817fa46a516d23a3cb2b7ff514426adbe4e9edd2f40346d622eb26",
    }
    payload = {"gender": "female", "status": "inactive"}
    response = requests.put(endpoint + f"{id_user}", json=payload, headers=headers)
    print(response.status_code)
    print(response.json())

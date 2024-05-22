import requests
from Utilities import config_reader

ENDPOINT = config_reader.readConfig("get_task", "url")


def test_get_task_rqst():
    task__id = "task_3a87358032c44c139aee76024da72a72"
    response = requests.get(ENDPOINT + f"{task__id}")
    data = response.json()
    # validate status code is 200
    assert response.status_code == 200
    # validate task_id received in response is same
    assert data['task_id'] == task__id

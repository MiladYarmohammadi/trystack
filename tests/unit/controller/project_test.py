import pytest

TEST_PROJECT_ID = ""


@pytest.mark.parametrize(
    ("headers", "data", "is_json", "status"),
    [
        ({}, "test", False, 415),
        ({"Content-Type": "application/json"}, "test", False, 400),
        ({"Content-Type": "application/json"}, {"name": 1}, True, 400),
        ({"Content-Type": "application/json"}, {"name": "test", "family": "tester"}, True, 400),
        ({"Content-Type": "application/json"}, {"name": "test"}, True, 201),
        ({"Content-Type": "application/json"}, {"name": "test"}, True, 409),
    ],
)
def test_create_project(client, headers, data, is_json, status):
    if is_json:
        response = client.post(
            "/api/v1/projects",
            json=data,
            headers=headers
        )
    else:
        response = client.post(
            "/api/v1/projects",
            data=data,
            headers=headers
        )
    if response.status_code == 201:
        global TEST_PROJECT_ID
        TEST_PROJECT_ID = response.get_json()["project"]["id"]
    assert response.status_code == status


@pytest.mark.parametrize(
    ("headers", "status"),
    [
        ({}, 415),
        ({"Content-Type": "application/json"}, 200)
    ],
)
def test_get_projects(client, headers, status):
    response = client.get(
        "/api/v1/projects",
        headers=headers
    )
    assert response.status_code == status


@pytest.mark.parametrize(
    ("headers", "project_id", "status"),
    [
        ({}, "test", 415),
        ({"Content-Type": "application/json"}, "test", 404),
        ({"Content-Type": "application/json"}, "TEST_PROJECT_ID", 200),
    ],
)
def test_get_project(client, headers, project_id, status):
    response = client.get(
        f"/api/v1/projects/{TEST_PROJECT_ID if project_id == 'TEST_PROJECT_ID' else project_id}",
        headers=headers
    )
    assert response.status_code == status


@pytest.mark.parametrize(
    ("headers", "project_id", "data", "is_json", "status"),
    [
        ({}, "test", "test", False, 415),
        ({"Content-Type": "application/json"}, "test", "test", False, 400),
        ({"Content-Type": "application/json"}, "test", {"name": 1}, True, 400),
        ({"Content-Type": "application/json"}, "test", {"status": ""}, True, 400),
        ({"Content-Type": "application/json"}, "test", {"status": -10}, True, 400),
        ({"Content-Type": "application/json"}, "test", {"status": 0, "family": "tester"}, True, 400),
        ({"Content-Type": "application/json"}, "test", {"status": 1}, True, 404),
        ({"Content-Type": "application/json"}, "TEST_PROJECT_ID", {"status": 1}, True, 200),
    ],
)
def test_update_project(client, headers, project_id, data, is_json, status):
    if is_json:
        response = client.patch(
            f"/api/v1/projects/{TEST_PROJECT_ID if project_id == 'TEST_PROJECT_ID' else project_id}",
            json=data,
            headers=headers
        )
    else:
        response = client.patch(
            f"/api/v1/projects/{TEST_PROJECT_ID if project_id == 'TEST_PROJECT_ID' else project_id}",
            data=data,
            headers=headers
        )
    assert response.status_code == status


@pytest.mark.parametrize(
    ("headers", "project_id", "status"),
    [
        ({}, "test", 415),
        ({"Content-Type": "application/json"}, "test", 404),
        ({"Content-Type": "application/json"}, "TEST_PROJECT_ID", 204),
    ],
)
def test_delete_project(client, headers, project_id, status):
    response = client.delete(
        f"/api/v1/projects/{TEST_PROJECT_ID if project_id == 'TEST_PROJECT_ID' else project_id}",
        headers=headers
    )
    assert response.status_code == status

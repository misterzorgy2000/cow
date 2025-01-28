# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.error_response import ErrorResponse  # noqa: F401
from openapi_server.models.model import Model  # noqa: F401
from openapi_server.models.short_model import ShortModel  # noqa: F401


def test_get_model_by_id(client: TestClient):
    """Test case for get_model_by_id

    
    """

    headers = {
        "x_auth_token": 'x_auth_token_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/v1/models/{model_id}".format(model_id='model_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_models(client: TestClient):
    """Test case for get_models

    
    """

    headers = {
        "x_auth_token": 'x_auth_token_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/v1/models",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


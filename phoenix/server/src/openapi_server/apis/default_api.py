# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.default_api_base import BaseDefaultApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.model import Model
from openapi_server.models.predict_request import PredictRequest
from openapi_server.models.prediction import Prediction
from openapi_server.models.short_model import ShortModel


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/v1/models/{model_id}",
    responses={
        200: {"model": Model, "description": "OK"},
        401: {"model": ErrorResponse, "description": "Unauthorized"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def get_model_by_id(
    x_auth_token: str = Header(None, description="Токен аутентификации"),
    model_id: str = Path(..., description="Id модели"),
) -> Model:
    """Получить данные о модели"""
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().get_model_by_id(x_auth_token, model_id)


@router.get(
    "/api/v1/models",
    responses={
        200: {"model": List[ShortModel], "description": "OK"},
        401: {"model": ErrorResponse, "description": "Unauthorized"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def get_models(
    x_auth_token: str = Header(None, description="Токен аутентификации"),
) -> List[ShortModel]:
    """Получить список моделей."""
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().get_models(x_auth_token)


@router.post(
    "/api/v1/predict/{model_id}",
    responses={
        200: {"model": Prediction, "description": "OK"},
        401: {"model": ErrorResponse, "description": "Unauthorized"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def predict(
    x_auth_token: str = Header(None, description="Токен аутентификации"),
    model_id: str = Path(..., description="Id модели"),
    cursor: str = Query(None, description="Курсор для получения следующей порции данных, для первого запроса должен передаваться пустым", alias="cursor"),
    predict_request: PredictRequest = Body(None, description=""),
) -> Prediction:
    """Сделать прогноз"""
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().predict(x_auth_token, model_id, cursor, predict_request)

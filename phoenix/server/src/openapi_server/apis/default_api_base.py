# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.model import Model
from openapi_server.models.predict_request import PredictRequest
from openapi_server.models.prediction import Prediction
from openapi_server.models.short_model import ShortModel

class BaseDefaultApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)
    async def get_model_by_id(
        self,
        x_auth_token: str,
        model_id: str,
    ) -> Model:
        """Получить данные о модели"""
        ...


    async def get_models(
        self,
        x_auth_token: str,
    ) -> List[ShortModel]:
        """Получить список моделей."""
        ...


    async def predict(
        self,
        x_auth_token: str,
        model_id: str,
        cursor: str,
        predict_request: PredictRequest,
    ) -> Prediction:
        """Сделать прогноз"""
        ...

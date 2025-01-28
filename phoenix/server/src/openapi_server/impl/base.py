# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.apis.default_api_base import BaseDefaultApi

from openapi_server.models.model import Model
from openapi_server.models.predict_request import PredictRequest
from openapi_server.models.prediction import Prediction
from openapi_server.models.short_model import ShortModel
import json
import os
import copy


class Impl(BaseDefaultApi):
    def __init__(self):
        with open('./mock/data.json', 'r') as file:
            self.data = json.load(file)

    async def get_model_by_id(
            self,
            x_auth_token: str,
            model_id: str,
    ) -> Model:
        return next(item for item in self.data['models'] if item["id"] == model_id)

    async def get_models(
            self,
            x_auth_token: str,
    ) -> List[ShortModel]:
        data = copy.deepcopy(self.data['models'])
        """Получить список моделей."""
        # define the keys to remove
        keys = ['description', 'score']

        for el in data:
            for key in keys:
                el.pop(key, None)

        return data

    async def predict(
            self,
            x_auth_token: str,
            model_id: str,
            cursor: str,
            predict_request: PredictRequest,
    ) -> Prediction:
        return self.data['predictions'][0]

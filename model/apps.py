from django.apps import AppConfig
from .model import dp_model


class ModelConfig(AppConfig):
    name = 'model'
    model_obj = dp_model()


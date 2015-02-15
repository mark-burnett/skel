from . import settings
import importlib
import os


settings.BASE_DIR = os.path.dirname(os.path.dirname(importlib.import_module(
    settings.SKEL_APP_MODULE).__file__))


# flake8: noqa

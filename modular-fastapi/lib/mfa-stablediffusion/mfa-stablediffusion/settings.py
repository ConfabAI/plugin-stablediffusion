import os

MODEL_DIRECTORY = os.environ.get("MODEL_DIRECTORY", None)

if MODEL_DIRECTORY is None:
    raise ValueError("MODEL_DIRECTORY environment variable is not set.")

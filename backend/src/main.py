import os
from fastapi import FastAPI

app = FastAPI()
# the or acts as a fallback in case the environment variable is not set, it will use the default value instead
MY_PROJ = os.environ.get("MY_PROJ") or "default_proj"
API_KEY = os.environ.get("API_KEY")

if not API_KEY:
    raise NotImplementedError("API_KEY environment variable is not set")

@app.get("/")
def read_index():
    return {"Hello": "World", "project-name": MY_PROJ, "API_KEY": API_KEY}
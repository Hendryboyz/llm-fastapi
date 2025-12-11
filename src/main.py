from typing import Union
from fastapi import FastAPI
from .config import get_settings

app = FastAPI()

@app.get('/health')
def health():
    return { 'status': 'ok' }
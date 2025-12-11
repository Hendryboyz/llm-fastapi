from typing import Union
from fastapi import FastAPI
from .config import get_settings
from .llm.router import router as llm_router

app = FastAPI()

app.include_router(llm_router)

@app.get('/health')
def health():
    return { 'status': 'ok' }
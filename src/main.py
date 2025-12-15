from fastapi import FastAPI
from contextlib import asynccontextmanager

from .ai.client import OpenAIClient
from .chat.router import router as llm_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    ai_client = OpenAIClient()
    app.state.ai_client = ai_client
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(llm_router)

@app.get('/health')
def health():
    return { 'status': 'ok' }
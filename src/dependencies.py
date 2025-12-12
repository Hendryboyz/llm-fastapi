from typing import Annotated
from fastapi import Depends, Request

from .ai.client import OpenAIClient

def get_ai_client(request: Request) -> OpenAIClient:
    return request.app.state.ai_client

AIClientDeps = Annotated[OpenAIClient, Depends(get_ai_client)]
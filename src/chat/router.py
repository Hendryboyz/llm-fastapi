from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse

from .schemas import CreateLLMGenerationRequest
from .service import create_reasoning_response
from ..dependencies import AIClientDeps
from .exceptions import DenyFormatException

router = APIRouter(
    prefix='/chat',
    tags=['chat'],
)

def generate_params(payload: CreateLLMGenerationRequest, format: bool = False):
    return {
        'prompt': payload.prompt,
        'format': format,
    }

@router.post('/generate')
def generate(
    payloads: Annotated[dict, Depends(generate_params)],
    ai_client: AIClientDeps = None
):
    response = create_reasoning_response(payloads['prompt'], format=payloads['format'], ai_client=ai_client)
    if payloads['format']:
        return response.output_parsed
    else:
        return response.output



@router.post('/generate/stream', response_class=StreamingResponse)
async def streaming_generate(
    payloads: Annotated[dict, Depends(generate_params)],
    ai_client: AIClientDeps = None
):
    if payloads['format']:
        raise DenyFormatException(error_code=1000001, status_code=422, error_message='Streaming is not supported for format response')
    response = create_reasoning_response(payloads['prompt'], stream=True, ai_client=ai_client)

    async def event_stream():
        for event in response:
            if getattr(event, 'type', None) == 'response.output_text.delta':
                print(event)
                yield f'data: {event.delta}\n\n'
    return StreamingResponse(event_stream(), media_type='text/event-stream')

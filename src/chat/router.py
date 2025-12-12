from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from .schemas import CreateLLMGenerationRequest
from .service import create_reasoning_response
from ..dependencies import AIClientDeps

router = APIRouter(
    prefix='/chat',
    tags=['chat'],
)

@router.post('/generate')
def generate(payload: CreateLLMGenerationRequest, ai_client: AIClientDeps = None):
    response = create_reasoning_response(payload.prompt, ai_client=ai_client)
    return response.output



@router.post('/generate/stream', response_class=StreamingResponse)
async def streaming_generate(payload: CreateLLMGenerationRequest, ai_client: AIClientDeps = None):
    response = create_reasoning_response(payload.prompt, stream=True, ai_client=ai_client)

    async def event_stream():
        for event in response:
            if getattr(event, 'type', None) == 'response.output_text.delta':
                print(event)
                yield f'data: {event.delta}\n\n'
    return StreamingResponse(event_stream(), media_type='text/event-stream')

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from .schemas import CreateLLMGenerationRequest
from .service import create_reasoning_response

router = APIRouter(
    prefix='/llm',
    tags=['llm'],
)

@router.post('/generate')
def generate(payload: CreateLLMGenerationRequest, format: str | None = None):
    response = create_reasoning_response(payload.prompt)

    return response.output



@router.post('/generate/stream', response_class=StreamingResponse)
async def streaming_generate(payload: CreateLLMGenerationRequest, format: str | None = None):
    response = create_reasoning_response(payload.prompt, stream=True)

    async def event_stream():
        for event in response:
            if getattr(event, 'type', None) == 'response.output_text.delta':
                print(event)
                yield f'data: {event.delta}\n\n'
    return StreamingResponse(event_stream(), media_type='text/event-stream')

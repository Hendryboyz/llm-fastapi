from pydantic import BaseModel

class CreateLLMGenerationRequest(BaseModel):
    prompt: str
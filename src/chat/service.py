from ..ai.client import OpenAIClient

def create_reasoning_response(
    prompt: str,
    stream: bool = False,
    format: bool = False,
    ai_client: OpenAIClient = None
):
    return ai_client.generate_response(prompt, stream=stream, format=format)
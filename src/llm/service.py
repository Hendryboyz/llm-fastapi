from openai import OpenAI

from ..config import get_settings

settings = get_settings()

client = OpenAI(api_key=settings.openai_api_key)

def create_reasoning_response(prompt: str, stream: bool = False):
    return client.responses.create(
        model='gpt-5-nano',
        instructions='像海盜一樣說話',
        reasoning={ 'effort': 'medium' },
        input=prompt,
        stream=stream,
    )
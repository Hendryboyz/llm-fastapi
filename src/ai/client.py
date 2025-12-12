from openai import OpenAI

from ..config import get_settings

class OpenAIClient:
    def __init__(self):
        settings = get_settings()
        self.client = OpenAI(api_key=settings.openai_api_key)
    
    def generate_response(self, prompt: str, model="gpt-5-nano", reasoning="medium", stream=False):
        return self.client.responses.create(
            model=model,
            instructions='像海盜一樣說話',
            reasoning={ 'effort': reasoning },
            input=prompt,
            stream=stream,
        )
    
    def __del__(self):
        self.client.close()
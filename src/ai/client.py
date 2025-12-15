from openai import OpenAI
from openai.types.shared import ResponsesModel
from pydantic import BaseModel

from ..config import get_settings

class CalendarSchedule(BaseModel):
    start_date: str
    end_date: str
    event_name: str
    description: str

class Step(BaseModel):
    explanation: str
    output: str

class MathReasoning(BaseModel):
    steps: list[Step]

class OpenAIClient:
    def __init__(self):
        settings = get_settings()
        self.client = OpenAI(api_key=settings.openai_api_key)
    
    def generate_response(self,
        prompt: str,
        model: ResponsesModel="gpt-5-nano",
        reasoning="medium",
        stream=False,
        format: bool = False
    ):
        if format:
            return self.client.responses.parse(
                model=model,
                reasoning={ 'effort': reasoning },
                input=[
                    {"role": "system", "content": "你是一個訓練有素的演算法講師，引導使用者一步一步實作演算法"},
                    {"role": "user", "content": prompt},
                ],
                stream=stream,
                text_format=MathReasoning,
            )
        else:
            return self.client.responses.create(
                model=model,
                reasoning={ 'effort': reasoning },
                instructions="你是一個訓練有素的演算法講師，引導使用者一步一步實作演算法",
                stream=stream,
                input=prompt,
            )
    
    def __del__(self):
        self.client.close()
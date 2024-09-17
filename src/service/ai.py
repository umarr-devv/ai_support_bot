from openai import AsyncOpenAI

from src.config import Config


class AiApiClient:

    def __init__(self, config: Config):
        self.client = AsyncOpenAI(
            api_key=config.ai_api.key,
            base_url=config.ai_api.url
        )
        self.model = config.ai_api.model

    async def completion(self, query: str, system_promt: str = '',
                         temperature: float = 0.7, max_tokens: int = 256):
        response = await self.client.chat.completions.create(
            messages=[
                {
                    'role': 'system',
                    'content': system_promt
                },
                {
                    'role': 'user',
                    'content': query
                }
            ],
            model=self.model,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content

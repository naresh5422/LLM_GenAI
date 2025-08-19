import os
from typing import Iterable
from openai import OpenAI
from config import settings

client = OpenAI(api_key = settings.OPENAI_API_KEY)

class OpenAIProvider:
    def stream_chat(self, messages):
        stream = client.chat.completions.create(model = settings.MODEL_NAME,
                                                messages = messages,
                                                stream = True,
                                                temperature=0.2)
        for chunk in stream:
            delta = chunk.choices[0].delta.content or ""
            if delta:
                yield delta

    def embed(self, texts):
        # Use text-embeddings-3-small by default
        resp = client.embeddings.create(model = 'text-embedding-3-small', input=texts) 
        res = [d.embeddings for d in resp.data]
        return res
from typing import List
import openai
import requests
import logging

from embeddingframework.adapters.base import EmbeddingAdapter

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class OpenAIEmbeddingAdapter(EmbeddingAdapter):
    """Adapter for OpenAI embeddings."""
    def __init__(self, model: str = "text-embedding-ada-002", api_key: str = None):
        self.model = model
        self.api_key = api_key or openai.api_key

    def embed(self, text: str) -> List[float]:
        try:
            response = openai.Embedding.create(model=self.model, input=text, api_key=self.api_key)
            return response['data'][0]['embedding']
        except Exception as e:
            logging.error(f"OpenAI embedding failed: {e}")
            raise

class HuggingFaceEmbeddingAdapter(EmbeddingAdapter):
    """Adapter for HuggingFace Inference API embeddings."""
    def __init__(self, model_url: str, api_token: str):
        self.model_url = model_url
        self.api_token = api_token

    def embed(self, text: str) -> List[float]:
        try:
            headers = {"Authorization": f"Bearer {self.api_token}"}
            response = requests.post(self.model_url, headers=headers, json={"inputs": text})
            response.raise_for_status()
            return response.json()[0]
        except Exception as e:
            logging.error(f"HuggingFace embedding failed: {e}")
            raise

class LocalEmbeddingAdapter(EmbeddingAdapter):
    """Adapter for local embedding models."""
    def __init__(self, model_callable):
        self.model_callable = model_callable

    def embed(self, text: str) -> List[float]:
        try:
            return self.model_callable(text)
        except Exception as e:
            logging.error(f"Local embedding failed: {e}")
            raise

from abc import ABC, abstractmethod
from typing import Iterable

class LLMProvider(ABC):
   @abstractmethod
   def stream_chat(self, messages: list[dict]) -> Iterable[str]:
       """
       Stream chat responses from the LLM.
       
       :param messages: List of message dictionaries to send to the LLM.
       :return: An iterable of response dictionaries.
       """
   @abstractmethod
   def embed(self, texts: list[str]) -> list[list[float]]:
         """
         Generate embeddings for a list of texts.
         
         :param texts: List of strings to embed.
         :return: List of embeddings, each embedding is a list of floats.
         """
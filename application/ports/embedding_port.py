from abc import ABC, abstractmethod
from typing import List


class EmbeddingPort(ABC):
    """Port for generating text embeddings"""
    
    @abstractmethod
    def embed(self, text: str) -> List[float]:
        """
        Generate embedding vector for given text
        
        Args:
            text: Text to embed
            
        Returns:
            List of floats representing the embedding vector
        """
        pass
    
    @abstractmethod
    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for multiple texts
        
        Args:
            texts: List of texts to embed
            
        Returns:
            List of embedding vectors
        """
        pass
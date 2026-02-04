from abc import ABC, abstractmethod
from typing import List
from domain.document.entities import Document


class LLMPort(ABC):
    """Port for Language Model operations"""
    
    @abstractmethod
    async def generate_answer(
        self, 
        question: str, 
        context: List[Document]
    ) -> str:
        """
        Generate an answer based on question and context documents
        
        Args:
            question: User's question
            context: Relevant documents for context
            
        Returns:
            Generated answer as string
        """
        pass
    
    @abstractmethod
    async def generate_answer_with_confidence(
        self,
        question: str,
        context: List[Document]
    ) -> tuple[str, float]:
        """
        Generate answer with confidence score
        
        Args:
            question: User's question
            context: Relevant documents for context
            
        Returns:
            Tuple of (answer, confidence_score)
        """
        pass
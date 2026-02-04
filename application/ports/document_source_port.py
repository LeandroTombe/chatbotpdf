from abc import ABC, abstractmethod
from typing import List
from domain.document.entities import Document


class DocumentSourcePort(ABC):
    """Port for loading documents from different sources"""
    
    @abstractmethod
    def load(self, reference: str) -> List[Document]:
        """
        Load documents from a source
        
        Args:
            reference: Path or reference to the document source
            
        Returns:
            List of Document entities
        """
        pass
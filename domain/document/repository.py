from abc import ABC, abstractmethod
from typing import List, Optional
from domain.document.entities import Document


class DocumentRepository(ABC):
    """Contrato para persistir/recuperar documentos"""
    
    @abstractmethod
    def save(self, documents: List[Document]) -> bool:
        """Save documents to storage"""
        pass
    
    @abstractmethod
    def find_by_id(self, doc_id: str) -> Optional[Document]:
        """Find document by ID"""
        pass
    
    @abstractmethod
    def search(self, query: str, limit: int) -> List[Document]:
        """Search documents by query"""
        pass
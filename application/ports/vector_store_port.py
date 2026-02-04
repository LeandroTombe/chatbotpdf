from abc import ABC, abstractmethod
from typing import List
from domain.document.entities import Document


class VectorStorePort(ABC):
    """Port for vector storage and similarity search operations"""
    
    @abstractmethod
    def store_embeddings(
        self, 
        documents: List[Document], 
        embeddings: List[List[float]]
    ) -> bool:
        """
        Store document embeddings in vector database
        
        Args:
            documents: List of documents to store
            embeddings: Corresponding embedding vectors
            
        Returns:
            True if successful, False otherwise
        """
        pass
    
    @abstractmethod
    def search_similar(
        self, 
        query_embedding: List[float], 
        k: int = 5
    ) -> List[Document]:
        """
        Search for similar documents using embedding vector
        
        Args:
            query_embedding: Query vector to search for
            k: Number of similar documents to return
            
        Returns:
            List of most similar documents
        """
        pass
    
    @abstractmethod
    def delete_all(self) -> bool:
        """
        Clear all documents from vector store
        
        Returns:
            True if successful, False otherwise
        """
        pass
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any, Optional


@dataclass
class Document:
    """Domain entity representing a document chunk"""
    
    content: str
    metadata: Dict[str, Any]
    page_number: int
    source: str
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    
    def __post_init__(self):
        """Validate document after initialization"""
        if not self.content:
            raise ValueError("Document content cannot be empty")
        if self.page_number < 0:
            raise ValueError("Page number must be non-negative")
        if not self.source:
            raise ValueError("Document source cannot be empty")
        
        # Set defaults if not provided
        if self.created_at is None:
            self.created_at = datetime.now()
    
    def get_preview(self, length: int = 200) -> str:
        """Get a preview of the document content"""
        if len(self.content) <= length:
            return self.content
        return self.content[:length] + "..."
    
    def word_count(self) -> int:
        """Get the number of words in the document"""
        return len(self.content.split())
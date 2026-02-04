from langchain_community.document_loaders import PyPDFLoader


class PDFLoader:
    """A class to handle PDF loading operations"""
    
    def __init__(self):
        """Initialize PDFLoader with empty documents list"""
        self.documents = []
    
    def load_pdf(self, file_path: str) -> bool:
        """
        Load a PDF file and store its documents
        
        Args:
            file_path: Path to the PDF file
            
        Returns:
            True if successful, False otherwise
        """
        try:
            loader = PyPDFLoader(file_path)
            self.documents = loader.load()
            return True
        except FileNotFoundError as e:
            print(f"Error: File not found - {e}")
            return False
        except Exception as e:
            print(f"Error loading PDF: {e}")
            return False
    
    def get_documents(self):
        """
        Get the loaded documents
        
        Returns:
            List of loaded documents
        """
        return self.documents


# Example usage (can be removed or kept for direct script execution)
if __name__ == "__main__":
    loader = PDFLoader()
    if loader.load_pdf("Paradigmas.pdf"):
        pages = loader.get_documents()
        print(f"Total pages: {len(pages)}")
        
        if pages:
            print(f"\nFirst page content:\n{pages[0].page_content[:500]}...")

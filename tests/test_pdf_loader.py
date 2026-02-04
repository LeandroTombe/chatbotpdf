import pytest
from unittest.mock import Mock, patch, MagicMock
from pdf_loader import PDFLoader


class TestPDFLoader:
    """Test suite for PDFLoader class"""
    
    def test_init_creates_empty_documents_list(self):
        """Test that PDFLoader initializes with empty documents list"""
        loader = PDFLoader()
        assert loader.documents == []
        assert isinstance(loader.documents, list)
    
    def test_load_pdf_success(self):
        """Test successful PDF loading"""
        loader = PDFLoader()
        mock_documents = [Mock(page_content="Test content", metadata={"page": 1})]
        
        with patch('pdf_loader.PyPDFLoader') as mock_pdf_loader:
            mock_loader_instance = Mock()
            mock_loader_instance.load.return_value = mock_documents
            mock_pdf_loader.return_value = mock_loader_instance
            
            result = loader.load_pdf("test.pdf")
            
            assert result is True
            assert loader.documents == mock_documents
            mock_pdf_loader.assert_called_once_with("test.pdf")
            mock_loader_instance.load.assert_called_once()
    
    def test_load_pdf_file_not_found(self):
        """Test PDF loading with non-existent file"""
        loader = PDFLoader()
        
        with patch('pdf_loader.PyPDFLoader') as mock_pdf_loader:
            mock_pdf_loader.side_effect = FileNotFoundError("File not found")
            
            result = loader.load_pdf("nonexistent.pdf")
            
            assert result is False
            assert loader.documents == []
    
    def test_load_pdf_general_exception(self):
        """Test PDF loading with general exception"""
        loader = PDFLoader()
        
        with patch('pdf_loader.PyPDFLoader') as mock_pdf_loader:
            mock_pdf_loader.side_effect = Exception("Unexpected error")
            
            result = loader.load_pdf("corrupted.pdf")
            
            assert result is False
            assert loader.documents == []
    
    def test_load_pdf_empty_path(self):
        """Test PDF loading with empty file path"""
        loader = PDFLoader()
        
        with patch('pdf_loader.PyPDFLoader') as mock_pdf_loader:
            mock_pdf_loader.side_effect = ValueError("Invalid file path")
            
            result = loader.load_pdf("")
            
            assert result is False
    
    def test_get_documents_after_successful_load(self):
        """Test getting documents after successful load"""
        loader = PDFLoader()
        mock_documents = [
            Mock(page_content="Page 1", metadata={"page": 1}),
            Mock(page_content="Page 2", metadata={"page": 2})
        ]
        
        with patch('pdf_loader.PyPDFLoader') as mock_pdf_loader:
            mock_loader_instance = Mock()
            mock_loader_instance.load.return_value = mock_documents
            mock_pdf_loader.return_value = mock_loader_instance
            
            loader.load_pdf("test.pdf")
            documents = loader.get_documents()
            
            assert documents == mock_documents
            assert len(documents) == 2
    
    def test_get_documents_before_load(self):
        """Test getting documents before loading any PDF"""
        loader = PDFLoader()
        documents = loader.get_documents()
        
        assert documents == []
        assert len(documents) == 0
    
    def test_multiple_pdf_loads_overwrites_documents(self):
        """Test that loading multiple PDFs overwrites previous documents"""
        loader = PDFLoader()
        
        first_docs = [Mock(page_content="First PDF")]
        second_docs = [Mock(page_content="Second PDF")]
        
        with patch('pdf_loader.PyPDFLoader') as mock_pdf_loader:
            # First load
            mock_loader_1 = Mock()
            mock_loader_1.load.return_value = first_docs
            
            # Second load
            mock_loader_2 = Mock()
            mock_loader_2.load.return_value = second_docs
            
            mock_pdf_loader.side_effect = [mock_loader_1, mock_loader_2]
            
            loader.load_pdf("first.pdf")
            assert loader.documents == first_docs
            
            loader.load_pdf("second.pdf")
            assert loader.documents == second_docs
            assert len(loader.documents) == 1
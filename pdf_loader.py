from langchain_community.document_loaders import PyPDFLoader

# Load PDF file
loader = PyPDFLoader("Paradigmas.pdf")
pages = loader.load()

# Print number of pages
print(f"Total pages: {len(pages)}")

# Print first page content
if pages:
    print(f"\nFirst page content:\n{pages[0].page_content[:500]}...")

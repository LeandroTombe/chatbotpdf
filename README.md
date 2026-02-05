# ChatbotPDF

PDF Chatbot with Clean Architecture.

## Project Structure

```
chatbot/
├── app/
│   ├── domain/           # Business logic and entities
│   ├── application/      # Use cases and ports
│   ├── infrastructure/   # External adapters
│   └── main.py
├── tests/
├── pyproject.toml
└── README.md
```

## Installation

```bash
pip install -e .
```

## Development

```bash
pip install -e ".[dev]"
pytest
```

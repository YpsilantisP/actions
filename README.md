# ⚙️ Actions

## 🚀 Getting Started

##### Set up your environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install poetry
poetry install
```

## 🧪 Running Tests Locally
poetry run pytest

## ⚡ Optional: Testing with DynamoDB Local
docker run -d -p 8000:8000 amazon/dynamodb-local

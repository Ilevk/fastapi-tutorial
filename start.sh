export ENV=local

poetry run uvicorn app.main:app --reload

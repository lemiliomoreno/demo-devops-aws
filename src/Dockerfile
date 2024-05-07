FROM python:3.11

WORKDIR /api

COPY . /api

RUN pip install --upgrade pip

RUN pip install poetry

RUN poetry install

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

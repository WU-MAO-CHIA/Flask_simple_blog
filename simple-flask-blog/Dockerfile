FROM python:3.13-slim

WORKDIR /app

RUN pip install uv --no-cache

COPY . .

RUN uv sync 

ENV FLASK_APP=app.py

CMD ["uv", "run", "flask", "run", "--host=0.0.0.0", "--port=5000"]
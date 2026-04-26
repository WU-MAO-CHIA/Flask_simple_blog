FROM python:3.13-slim

WORKDIR /app

RUN pip install uv 
COPY pyproject.toml uv.lock ./
RUN uv pip install --system .

COPY . .

ENV FLASK_APP=app.py

EXPOSE 8000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]

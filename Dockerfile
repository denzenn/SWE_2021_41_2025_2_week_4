FROM python:3.12-slim

COPY ishappy.py /app/ishappy.py
CMD ["python", "/app/ishappy.py"]


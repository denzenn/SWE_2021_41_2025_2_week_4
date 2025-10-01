FROM python:3.12

COPY ishappy.py /app/ishappy.py
CMD ["python", "/app/ishappy.py"]


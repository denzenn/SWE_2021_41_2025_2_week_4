FROM python:3.12-slim
COPY app.py /app.py
CMD ["python", "/app.py"]

FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml ./
COPY api ./api
RUN pip install --no-cache-dir .
ENV PORT=8080
EXPOSE 8080
CMD ["sh", "-c", "uvicorn api.main:app --host 0.0.0.0 --port ${PORT}"]

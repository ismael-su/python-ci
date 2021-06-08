FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

EXPOSE 8080
COPY ./app /app

CMD ["uvicorn", "index:app", "--reload", "--host", "0.0.0.0","--port","2376"]

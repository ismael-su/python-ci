FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt /app


RUN pip install --no-cache-dir --upgrade pip

EXPOSE 8080
COPY ./ /app

CMD ["uvicorn", "app.index:app", "--reload", "--host", "0.0.0.0","--port","2376"]

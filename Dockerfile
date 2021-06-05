FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt /app


RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
COPY ./ /app

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0","--port","2376"]

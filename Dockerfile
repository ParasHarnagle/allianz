FROM tiangolo/uvicorn-gunicorn:python3.10-slim

WORKDIR /app

COPY . /app

EXPOSE 8085

RUN pip install -r requirements.txt

CMD ["uvicorn","app.main:app", "--host","0.0.0.0","--port","8085"]

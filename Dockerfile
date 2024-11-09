FROM python:3.13-bullseye

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir Flask

EXPOSE 5000

CMD ["python", "app.py"]
FROM python:3.8-bullseye
EXPOSE 8000
WORKDIR /App
COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt --no-cache-dir
COPY . .

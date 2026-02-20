FROM python:3.13-bookworm
COPY requirements.txt /
RUN pip install -r requirements.txt
RUN mkdir app
WORKDIR app
COPY . .
ENTRYPOINT ["python", "main.py", "--period", "60", "--currency", "USD"]
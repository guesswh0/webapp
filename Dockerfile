FROM python:3.9-slim
EXPOSE 8080
WORKDIR /usr/src/app
COPY src .
CMD ["python", "run.py"]

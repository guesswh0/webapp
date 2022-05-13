FROM python:alpine
EXPOSE 8080
WORKDIR /usr/src/app
COPY src .
CMD ["python", "run.py"]

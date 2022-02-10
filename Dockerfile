FROM python:3.8-slim
EXPOSE 5001
WORKDIR /usr/src/app
RUN pip install --no-cache-dir gunicorn
COPY src .
CMD ["gunicorn", "-b", ":5001", "app"]

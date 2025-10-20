FROM python:3.9-slim-buster
WORKDIR /webapp1
COPY . /webapp1
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD [ "python3","app.py" ]
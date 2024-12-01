FROM python:3.13-alpine

WORKDIR /opt/app
COPY . .
EXPOSE 3101
RUN pip3 install -r requirements.txt
CMD ["python3", "server.py"]
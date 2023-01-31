FROM alpine:latest
RUN apk update
RUN apk add py-pip
RUN apk add --no-cache python3-dev 
RUN pip install --upgrade pip
RUN python3 -m pip install flask
RUN python3 -m pip install datetime
WORKDIR /app
COPY . /app 
CMD ["python3", "app.py"]


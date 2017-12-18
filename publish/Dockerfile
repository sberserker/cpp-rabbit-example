FROM alpine:3.1

# Update
RUN apk add --update python py-pip

WORKDIR /app
ADD main.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

EXPOSE  8000

CMD ["python", "./main.py", "-p 8000"]

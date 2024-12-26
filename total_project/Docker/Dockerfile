FROM python:3.10
WORKDIR /usr/src/app
COPY ./src/ ./
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python3", "./var2.py" ]


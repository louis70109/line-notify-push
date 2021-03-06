FROM python:3.7
WORKDIR /app
COPY ["requirements.txt", "/app/"]
RUN python3 -m pip install -r requirements.txt
ADD . /app
ENTRYPOINT ["python3", "main.py"]
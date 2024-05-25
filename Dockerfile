FROM  python:3.11.9-slim-buster
WORKDIR /service

# the last . is used to use workdirectory
COPY requirements.txt .
# . show the local directory and ./ represent the working directory(current directory)
COPY . ./


RUN pip install -r requirements.txt

ENTRYPOINT [ "python3","app.py" ]
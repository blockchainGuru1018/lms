FROM python:3.8-slim-buster

WORKDIR /app

COPY src/requirements.txt ./
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r ./requirements.txt

# COPY [src] .
# CMD ["python3.8", "src/manage.py", "runserver"]
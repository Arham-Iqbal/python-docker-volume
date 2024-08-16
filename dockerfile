FROM python:latest
WORKDIR /PYTHON-VOLUME
COPY . .
CMD [ "python","a.py" ]

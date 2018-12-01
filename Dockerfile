FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY __MY_APP__ ./__MY_APP__

CMD [ "python", "-m", "__MY_APP__" ]

FROM python:2.7

RUN mkdir -p /usr/src/reddit-notifier
WORKDIR /usr/src/reddit-notifier
COPY . /usr/src/reddit-notifier
COPY requirements.txt  /usr/src/reddit-notifier/
COPY . /usr/src/reddit-notifier/
EXPOSE 80
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./Rising_Text_Runnable.py" ]

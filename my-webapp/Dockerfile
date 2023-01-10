FROM ubuntu 

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip install flask
RUN pip install gunicorn

COPY app.py /opt/app.py

CMD ["run", "gunicorn", "-w", "4", "/opt.app:create_app"]

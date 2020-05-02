FROM centos:latest

RUN yum update -y && yum install -y python3

WORKDIR /root

COPY application.py requirements.txt templates /root/

RUN pip3 install -r requirements.txt


EXPOSE 5000

ENTRYPOINT [ "python3", "application.py" ]

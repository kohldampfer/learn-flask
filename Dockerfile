FROM centos:latest

RUN yum update -y && yum install -y python3

ADD application.py /root/
ADD requirements.txt /root/

RUN pip3 install -r requirements.txt

WORKDIR /root

EXPOSE 5000

ENTRYPOINT [ "python3", "appliation.py" ]

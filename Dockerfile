FROM centos:7

COPY requerimientos.txt requerimientos.txt
RUN yum update -y && yum install -y epel-release && yum install -y python-pip
RUN pip install -r  requerimientos.txt
COPY comotedicenapp comotedicenapp
WORKDIR  comotedicenapp
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

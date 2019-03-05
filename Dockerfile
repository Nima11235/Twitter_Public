FROM centos/python-27-centos7 

USER root
COPY requirements.txt /deployments/
COPY twitterexample.py  /deployments/
COPY sentiment.py /deployments/
COPY AFINN-111.txt /deployments/

RUN yum -y install epel-release
RUN yum -y install python-devel
RUN yum -y install python-pip
ENV LD_LIBRARY_PATH=/opt/rh/python27/root/usr/lib64
RUN pip install --no-cache-dir -r /deployments/requirements.txt


CMD cd /deployments; bash


FROM ubuntu:20.04
RUN apt-get -y update
RUN apt-get -y install python3-pip
WORKDIR /work
COPY app/requirements.txt /work/requirements.txt
COPY app/start.py /work/start.py
COPY app/start.py /work/start.py
COPY app/sweater/ /work/sweater/
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD python3 start.py

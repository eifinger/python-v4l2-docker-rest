FROM ubuntu:16.04

RUN apt-get update -qq  \
	&& apt-get install -y libv4l-dev \
	&& apt-get install -y libjpeg8-dev \
    && apt-get install -y git \
    && apt-get install -y python-pip

RUN pip install "django<2" Image==1.5.27 flask==1.0.2

RUN git clone https://github.com/gebart/python-v4l2capture.git

RUN mkdir -p /capture

WORKDIR /python-v4l2capture
RUN ./setup.py install
COPY app.py app.py
WORKDIR /capture
CMD python ../python-v4l2capture/app.py
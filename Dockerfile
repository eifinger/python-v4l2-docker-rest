FROM ubuntu

RUN apt-get update -qq  \
	&& apt-get install -y libv4l-dev \
	&& apt-get install -y libjpeg8-dev \
    && apt-get install -y git \
    && apt-get install -y python3-pip \
    && pip install Image aiohttp \
    && git clone https://github.com/gebart/python-v4l2capture.git \
    && mkdir -p /capture
WORKDIR /python-v4l2capture
RUN ./setup.py install
COPY app.py app.py
WORKDIR /capture
CMD python3 ../python-v4l2capture/app.py
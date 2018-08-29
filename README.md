python-v4l2-docker-rest
=================

eifinger/python-v4l2-docker with a rest interface

##Usage

``sudo docker run --device=/dev/video0 -v <image directory>:/capture -it --name <container name> eifinger/python-v4l2-docker-rest``
For example:  
``sudo docker run --device=/dev/video0 -v /home/eifinger/python-v4l2-docker-rest/capture:/capture -it --name python-v4l2-docker-rest eifinger/python-v4l2-docker-rest``

## Links
- eifinger/python-v4l2-docker <https://github.com/eifinger/python-v4l2-docker>
- gebart/python-v4l2capture: <https://github.com/gebart/python-v4l2capture>

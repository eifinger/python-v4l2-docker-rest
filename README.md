python-v4l2-docker-rest
=================

eifinger/python-v4l2-docker with a rest interface

##Usage

``sudo docker run --device=/dev/video0 -v <image directory>:/capture -it --name <container name> eifinger/python-v4l2-docker-rest``
For example:  
``sudo docker run -d --device=/dev/video0 -v /home/admin/python-v4l2-docker-rest/capture:/capture -p 9922:8080 --name python-v4l2-docker-rest eifinger/python-v4l2-docker-rest``

``wget -O image.jpg http://192.168.0.2:9922/getImage``

## Links
- eifinger/python-v4l2-docker <https://github.com/eifinger/python-v4l2-docker>
- gebart/python-v4l2capture: <https://github.com/gebart/python-v4l2capture>

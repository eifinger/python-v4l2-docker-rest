from PIL import Image
import select
import v4l2capture
import time
import logging
from flask import Flask, send_file
import os

__VERSION__ = "0.1"
__LOGGER_NAME__ = "python-v4l2-docker-rest"
app = Flask(__name__)

def main():
    """
    Main function

    Returns:
        None

    Raises:
        Exception: Raises an exception.
    """
    global logger
    logger = setup_logger()
    logger.info("Running Version: {}".format(__VERSION__))

    logger.info("Starting WebServer...")
    app.run(host='0.0.0.0', port=8080, debug=False)

@app.route('/image', methods=['GET'])
def getImage():
    filename = takeImage()
    try:
        return send_file(filename, attachment_filename=os.path.split(filename)[1])
    except Exception as e:
        return str(e)

def takeImage():
    # Open the video device.
    video = v4l2capture.Video_device("/dev/video0")
    
    # Suggest an image size to the device. The device may choose and
    # return another size if it doesn't support the suggested one.
    size_x, size_y = video.set_format(1280, 1024)
    
    # Create a buffer to store image data in. This must be done before
    # calling 'start' if v4l2capture is compiled with libv4l2. Otherwise
    # raises IOError.
    video.create_buffers(1)
    
    # Send the buffer to the device. Some devices require this to be done
    # before calling 'start'.
    video.queue_all_buffers()
    
    # Start the device. This lights the LED if it's a camera that has one.
    video.start()
    
    # Wait for the device to fill the buffer.
    select.select((video,), (), ())
    
    # The rest is easy :-)
    image_data = video.read()
    video.close()
    image = Image.frombytes("RGB", (size_x, size_y), image_data)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = "/capture/image_" + timestr + ".jpg"
    image.save(filename)
    logger.info("Saved " + filename + "(Size: " + str(size_x) + " x " + str(size_y) + ")")
    return filename

def setup_logger():
    logger = logging.getLogger(__LOGGER_NAME__)
    logger.setLevel(logging.DEBUG)
    # create console handler with a log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(ch)
    return logger

if __name__ == "__main__":
    main()
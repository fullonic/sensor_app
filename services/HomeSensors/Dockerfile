# base python image
FROM python:3.7.3-alpine

# install dependencies
RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev bash && \
    apk add postgresql-dev && \
    apk add netcat-openbsd libffi-dev

# SET WORKING DIR
WORKDIR /home/HomeSensors/app

# ADD AND INSTALL REQUIREMENTS
COPY ./requirements.txt /home/HomeSensors/app/requirements.txt
RUN pip install -r requirements.txt

# ADD ENTREYPOINT AND MAKE IT EXEC
COPY ./entrypoint.sh /home/HomeSensors/app/entrypoint.sh
RUN chmod +x /home/HomeSensors/app/entrypoint.sh

# COPY APP DIR TO DOCKER CONTAINER
COPY . /home/HomeSensors/app

# INSTALL DHT SENSOR DRIVER ONLY WORKS WHEN BUILDING IN RASPBERY DEVICE.
# WHEN RUNNING DEV MACHINE IT WILL IGNORE ERROR AND EXIT WITH CODE 0
RUN cd app/sensors/drivers/Adafruit_Python_DHT && python setup.py install; exit 0
# RUN SERVER
CMD ["/home/HomeSensors/app/entrypoint.sh"]

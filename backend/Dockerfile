#declare the base image
#from image_name:tag
FROM python:latest

# host.docker.internal instead of localhost, this is because the container has its own network and cannot access the host machine's network directly, so we use host.docker.internal to access the host machine's network from within the container. This is especially important for accessing the database service that is running on the host machine, which is necessary for the backend application to function properly.
# curl -X POST -d '{"message": "Hello, World!"}' http://host.docker.internal:8080/api/chats/
RUN apt-get update && apt-get install -y curl

# Create a python virtual environment (optional but recommended)
# this is to isolate the dependencies of the application from the system python
RUN python -m venv /opt/venv/
# this creates the virtual environment in the /opt/venv directory within the container
ENV PATH=/opt/venv/bin:$PATH

WORKDIR /app
COPY requirements.txt /tmp/requirements.txt
# RUN within container while building the image, install the dependencies from the requirements.txt file    
RUN /opt/venv/bin/pip install -r /tmp/requirements.txt
COPY ./src .

# to run a server on a container you need to tell the computer it is okay for docker to run the server:
# docker run -it -p "port_number":"port_out" image_name
CMD [ "python", "-m", "http.server", "8000" ]


# docker compose run backend /bin/bash
# cd /opt/venv/bin
# ls
# this shows all of the different executables that are available in the virtual environment, including pip and pythonssh-keygen -t ed25519 -C "your_email@example.com"

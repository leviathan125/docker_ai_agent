#declare the base image
#from image_name:tag
FROM python:latest

WORKDIR /app
# linux command to create a file called index.html and write "hello" in it


# COPY local_file_path container_file_path
# RUN mkdir -p /static_folder
# COPY ./static_html /static_folder 

# same destination
COPY ./src .
# COPY ./static_html /app


# RUN echo "hello" > index.html 



#docker build -f DockerFile -t test_app .
#docker run -it -p 2000:8000 test_app

#docker build -f DockerFile -t codingforentrepreneurs/ai-py-app-test:v1 .
#docker push codingforentrepreneurs/ai-py-app-test:v1

# to run a server on a container you need to tell the computer it is okay for docker to run the server:
# docker run -it -p "port_number":"port_out" image_name
CMD [ "python", "-m", "http.server", "8000" ]

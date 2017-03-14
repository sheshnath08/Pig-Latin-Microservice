# Pig-Latin-Translation
The service is build on the flask framework and within Docker container. This service can be used to translate sentence into Pig Latin.

#Retrieve code

    $ git clone https://github.com/sheshnath08/Pig-Latin-Microservice.git
    $ cd Pig-Latin-Microservice

#Installation
**Building**

    Install Docker and Docker Compose.
    $ docker-compose build

**Running**

Run Docker development server

   `` $ docker-compose up`` https://docs.docker.com/compose/reference/up/

**Stopping**

Stop Docker development server

  ``$ docker-compose stop`` https://docs.docker.com/compose/reference/stop/

**Removing**

Remove Docker development server

   `$ docker-compose down` https://docs.docker.com/compose/reference/down/

**Accessing a container**

You can access shell in a container

   ` $ docker exec -i -t <CONTAINER_NAME_OR_ID> /bin/bash`

E.g.

    $ docker ps # get the name from the list of running containers
    $ docker exec -i -t pig_latin_microservices /bin/bash

#Testing
You can run the unit tests, which are in the tests directory of the project.
**Installing Dependencies**
 Run this command to install dependencies for the test.
 `$ pip install -r requirements.txt`
 
**Running tests**

`$ python tests/translation_test.py`



_**Readme Notes**_

    If the command line starts with $, the command should run with user privileges
    If the command line starts with #, the command should run with root privileges

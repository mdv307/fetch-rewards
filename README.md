# fetch-rewards Exercise

Program to check the health of a set of HTTP endpoints

<br>

## Prerequisites

- [Docker](https://www.docker.com/)

<br>

## Getting Started

These instructions will guide you on how to run the Python script in a Docker container.

###   1. Add input file 
    Add required input file containing all the urls in the main directory as "input.yaml"

###   2. Build the Docker Image

&nbsp; Navigate to the project directory and run the following command to build the Docker image:


    docker build -t fetch .

###   3. Run the Docker Container
Once the image is built, run the Docker container:

```bash
docker run fetch
```

<br>

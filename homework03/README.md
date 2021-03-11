# Moreau Flask App

This is a Flask app for homework 3 that returns different animals.

## Installation

The program is contained in a Docker container. The dockerfile and requirements.txt are included in this repository.

Download the files to your local machine and build the Docker container.

```bash
docker build -t <name of docker image> <path to dockerfile>
```
Ensure that ```requirements.txt``` is in the same folder as the dockerfile.

Run the container.

```bash
docker run -d -p <your port number>:5000 <name of docker image>
```

A Flask server is now running on your port number.

## Usage

The server is using HTTPS. ```curl``` is the command demonstrated here, but there are other ways to interact with the server.

```bash
curl localhost:<your port number>/<route>
curl localhost:5033/hello    # example: returns "Hello world!"
```

### Routes

####  ```/animals```

Returns all Moreau animals as JSON-formatted list.

#### ```/animals/<part>/<kind>```

Returns all animals with value ```<kind>``` of attribute ```<part>```.

Example: ```curl localhost:5033/animals/arms/10```

#### ```/animals/contains/<word>```
Returns all animals that have attributes that contain the string ```<word>```.

Example: ```curl localhost:5033/animals/contains/bird```

## License
[MIT](https://choosealicense.com/licenses/mit/)

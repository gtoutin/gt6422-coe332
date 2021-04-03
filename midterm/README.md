# Moreau Flask App with Redis Database

This is a Flask app that interacts with a Redis database to store, edit, and return animals.

## Installation

Installation is simple. Copy over the midterm folder and enter it. Once inside, start up the containers with docker-compose.

```bash
cd midterm
docker-compose up --build
```

## Usage

To all possible routes of the Flask app and what they do, hit the / route of the app for the front page.
```bash
curl localhost:5033/
```

Before any of the ```/animals/...``` routes can be used, you must first load the data from the example ```animals.json``` provided.
```bash
curl localhost:5033/animals/loaddata
```
### Note:
If different animals are needed, the ```animals.json``` file can be produced with the provided ```generate_animals.py``` script with ```python3 ./app/generate_animals.py```

### For the midterm, the routes of interest are
- ```/animals/dates/<date1>/<date2>``` to query a range of dates
- ```/animals/uuid/<uuid>``` selects a particular creature from its unique identifier
- ```/animals/edit/<uuid>?<stat>=<value>``` edits a particular creature by passing the UUID, and updated “stats”.  
(Note: the ```created_on``` stat can be edited in the ```YYYY-MM-DD%20HH:MM:SS.XXXXXX``` format for ease of testing the date features)
- ```/animals/delete/<date1>/<date2>``` deletes a selection of animals by a date range
- ```/animals/avglegs``` returns the average number of legs per animal
- ```/animals/count``` returns the total count of animals

## Stopping
Once finished with the app, the Docker containers must be stopped and then removed.
```bash
docker stop gctoutin-flask
docker stop gctoutin-redis
docker rm gctoutin-flask
docker rm gctoutin-redis
```
Their deletion can be confirmed with ```docker ps -a```

## License
[MIT](https://choosealicense.com/licenses/mit/)

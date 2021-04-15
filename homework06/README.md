# Deploying a Flask API to Kubernetes

This is a Flask app that interacts with a Redis database to store, edit, and return animals. It is defined in Kubernetes with these yml files.

## Installation

Installation is simple. Copy over the homework06 folder and enter it. Once inside, start up the containers with kubectl.

```bash
cd homework06
kubectl apply -f gctoutin-test-redis-pvc.yml
kubectl apply -f gctoutin-test-redis-deployment.yml
kubectl apply -f gctoutin-test-redis-service.yml
kubectl apply -f gctoutin-test-flask-deployment.yml
kubectl apply -f gctoutin-test-flask-service.yml
```

## Usage

To use the Flask service, you need the IP address of the Flask service.
```bash
kubectl get services -o wide
```
Example output:
```
NAME                          TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE     SELECTOR
gctoutin-flask-service-test   ClusterIP   10.101.5.231     <none>        5000/TCP         10h     app=gctoutin-test-flask
gctoutin-service-test         ClusterIP   10.98.218.97     <none>        6379/TCP         8d      app=gctoutin-test-redis
```

You will also need a Python debug pod to access this IP address from inside the cluster. This pod contains an environment that can access the Flask API.
```bash
kubectl apply -f deployment-python-debug.yml
kubectl get pods -o wide
kubectl exec -it <name of python pod from previous output> -- /bin/bash
```

To get all possible routes of the Flask app and what they do, hit the / route of the app for the front page.
```bash
curl 10.101.5.231:5000/
```

Before any of the ```/animals/...``` routes can be used, you must first load the data from the example ```animals.json``` provided.
```bash
curl 10.101.5.231:5000/animals/loaddata
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

# learn-flask-json
A simple example using flask with json

# Starting

Generating docker image
```
docker build -t flask_json .
```

Running docker image
```
docker run -it -d -p 5000:5000 flask_json
```

Calling `/echo` method
```
curl -X POST --data "{\"message\": \"hi\"}" --header "Content-Type: application/json" localhost:5000/echo
```

## To build:

```
  docker build -t websockets-test:1.0 .
```

## To start
```
  docker run -d --name run-websockets-test --publish 8765:8765 --rm \
    websockets-test:1.0
```

## To connect
```
  python -m websockets ws://localhost:8081/
```
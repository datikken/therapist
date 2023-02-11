docker build -t websockets-test:1.0 .;

docker run -d --name run-websockets-test --publish 8765:8765 --rm \
  websockets-test:1.0
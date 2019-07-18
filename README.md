# Fastparquet crashes in official Python 3.7.4 docker image
To reproduce, run
```
docker build -t test-fpq .
docker run test-fpq
```
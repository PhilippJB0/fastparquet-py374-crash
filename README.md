# Fastparquet crashes in official Python 3.7.4 docker image
To reproduce, run
```
docker build -t test-fpq .
docker run test-fpq
```
Output:
```
$ docker run test-fpq
Creating dataframe
Saving dataframe
Done
Segmentation fault (core dumped)
$ echo $?
139
```
#!/bin/sh -xe


OS_VERSION=$1

# This script starts docker and systemd (if el7)

docker run --privileged -d -ti -e "container=docker"  -v /sys/fs/cgroup:/sys/fs/cgroup -v `pwd`:/clank:rw  centos:centos${OS_VERSION}   /usr/sbin/init
DOCKER_CONTAINER_ID=$(docker ps | grep centos | awk '{print $1}')
docker logs $DOCKER_CONTAINER_ID
docker exec -ti $DOCKER_CONTAINER_ID /bin/bash -xec "bash -xe /clank/test_inside_docker.sh ${OS_VERSION};
  echo -ne \"------\nEND CLANK TESTS\n\";"
docker ps -a
docker stop $DOCKER_CONTAINER_ID
docker rm -v $DOCKER_CONTAINER_ID

fi
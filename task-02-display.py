# Python script for showing running services and containers
# usage: python task-02-display.py  

# loading modules
import docker

# setting up client 
client = docker.from_env()

# show services
print client.services.list()
print client.containers.list(all=True)
# docker-demo-todo-app
Official Repo of project

# Docker Commands
1. docker build --tag python-todoapp-docker . (build the docker)
2. docker images (list out all docker images)
3. docker run -d -p 5000:5000 python-todoapp-docker (run docker image)
4. docker ps (docker running status)
5. docker stop <container-name> (stop docker)
6. docker tag python-todoapp-docker:latest madhupiot/python-todoapp-docker (giving some docker tag)
7. docker push madhupiot/python-todoapp-docker (pushing to my dockerhub)

# AWS Commands
1. sudo apt-get update
2. sudo apt-get upgrade -y
3. curl -fsSL https://get.docker.com -o get-docker.sh
4. sh get-docker.sh
5. sudo docker version
6. sudo docker push madhupiot/python-todoapp-docker
7. sudo docker run -d -p 5000:5000 madhupiot/python-todoapp-docker
8. sudo docker ps

# Postman Requests
1. http://aws-public-ip:5000/
2. http://aws-public-ip:5000/items/all
3. http://aws-pubic-ip:5000/item/new (key: item, value: project abstract)
4. http://aws-public-ip:5000/item/status (key: item, value: project abstract)
5. http://aws-public-ip:5000/item/update (key: item, value: project abstract, key: status, value: in progress)
6. http://aws-public-ip:5000/item/remove (key: item, value: project abstract)


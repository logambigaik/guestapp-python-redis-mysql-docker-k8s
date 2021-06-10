# Scenario
```
A member of your team has developed a self-contained Very Exciting Guestbook in Python that requires deployment to a Production environment so the general public can visit it.
The Guestbook consists of 3 pages:
● a home page where visitors are invited to enter their name and keeps a count of the number of page views
● a submission/'Thanks' page for visitors that have entered their name
● a 'Visitors' page where previous visitors to the website are listed
Names of visitors to the site are stored in MySQL, and number of page views are stored in redis.

```

https://github.com/janakiramm/Kubernetes-multi-container-pod.git

https://testdriven.io/blog/running-flask-on-docker-swarm/#automation-script

https://github.com/logambigaik/ecs_nodejs
https://github.com/logambigaik/codedeploy-springboot.git

https://www.infoq.com/articles/aws-codepipeline-deploy-docker/

https://kublr.com/blog/setting-up-mysql-replication-clusters-in-kubernetes-2/


https://www.stacksimplify.com/aws-eks/microservices-on-aws-eks/learn-to-deploy-microservices-on-aws-eks/  --k8s

```
https://github.com/logambigaik/guestapp-python-redis-mysql-docker-k8s.git

aws codepipeline get-pipeline --name guestapp-pipeline >pipeline.json

in buildspec.yaml



artifacts:
  files:
    - appspec.yml
    - target/SampleMavenTomcatApp.war
    - scripts/*
    
 ```

# Docker-compose:

```

sudo amazon-linux-extras install -y docker && sudo service docker start && sudo usermod -a -G docker ec2-user && sudo chkconfig docker on && sudo yum install -y git && sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose && docker-compose version && sudo reboot

 ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
 docker-compose --version
```

```
docker-compose up
[root@ip-172-31-84-176 guestapp-python-redis-mysql-docker-k8s]# docker-compose ps
root@5e030756576f:/# mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 3
Server version: 5.7.34 MySQL Community Server (GPL)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| guestapp           |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.01 sec)

mysql> use guestapp;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A
Database changed

mysql> select * from guestbook;
+--------------+---------------+
| visitor_name | visitor_count |
+--------------+---------------+
| Loga         |             2 |
+--------------+---------------+
1 row in set (0.00 sec)

```
![image](https://user-images.githubusercontent.com/54719289/120852752-88fa9800-c572-11eb-9ee4-a3a1107cddd9.png)

![image](https://user-images.githubusercontent.com/54719289/120852919-ce1eca00-c572-11eb-9021-201aa75b498c.png)
![image](https://user-images.githubusercontent.com/54719289/120852949-dc6ce600-c572-11eb-86e9-12b51060779f.png)


# For docker-stack push the image into docker repo/ecr:

```
[root@ip-172-31-84-176 guestapp-python-redis-mysql-docker-k8s]# docker build -t klogambigai/guestapp_pythonweb:latest -f ./app/Dockerfile ./app
Sending build context to Docker daemon  9.728kB
Step 1/6 : FROM python:3.4-alpine
 ---> c06adcf62f6e
Step 2/6 : ADD . /code
 ---> Using cache
 ---> 4696839a0c51
Step 3/6 : WORKDIR /code
 ---> Using cache
 ---> 6bba3a19f7b3
Step 4/6 : RUN pip install -r requirements.txt
 ---> Using cache
 ---> d713cd794b6a
Step 5/6 : EXPOSE 8000
 ---> Using cache
 ---> efe8b00e2a20
Step 6/6 : CMD ["python", "app.py"]
 ---> Using cache
 ---> 5984b46512e0
Successfully built 5984b46512e0
Successfully tagged klogambigai/guestapp_pythonweb:latest
[root@ip-172-31-84-176 guestapp-python-redis-mysql-docker-k8s]# docker build -t klogambigai/guestapp_mysqldb:latest -f ./db/Dockerfile ./db
Sending build context to Docker daemon  3.072kB
Step 1/2 : FROM mysql:5.7
 ---> 2c9028880e58
Step 2/2 : ADD dbinit.sql /docker-entrypoint-initdb.d
 ---> Using cache
 ---> 55db777f5a5f
Successfully built 55db777f5a5f
Successfully tagged klogambigai/guestapp_mysqldb:latest

```


# Docker Machine Installation:

```
 base=https://github.com/docker/machine/releases/download/v0.16.0   && curl -L $base/docker-machine-$(uname -s)-$(uname -m) >/tmp/docker-machine   && sudo mv /tmp/docker-machine /usr/local/bin/docker-machine   && chmod +x /usr/local/bin/docker-machine

 ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
 
 docker-machine version
 
```

# Dockerswarm:

# Open the port 2377 in docker master

```
[root@ip-172-31-84-176 opt]# docker swarm init
Swarm initialized: current node (sm6ivmg1iizh9i3tyf1dk82xi) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-335datyte9oqg656hp10o461if1krm132eri9j2z9qiyiu6say-a9yqdl8mmwro87xpcgjjocmzk 172.31.84.176:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.

```
![image](https://user-images.githubusercontent.com/54719289/120864464-2ad6b080-c584-11eb-8748-2dff9ae7182f.png)



# Docker visualizer:

![image](https://user-images.githubusercontent.com/54719289/120867457-de8e6f00-c589-11eb-94b3-b12a9861d18b.png)

```
docker stack --compose-file=docker-stack.yaml guestapp

docker service ps guestap

docker service scale guestapp_web=3
```

# Scenario
```
A member of your team has developed a self-contained Very Exciting Guestbook in Python that requires deployment to a Production environment so the general public can visit it.
The Guestbook consists of 3 pages:
● a home page where visitors are invited to enter their name and keeps a count of the number of page views
● a submission/'Thanks' page for visitors that have entered their name
● a 'Visitors' page where previous visitors to the website are listed
Names of visitors to the site are stored in MySQL, and number of page views are stored in redis.

```


https://www.infoq.com/articles/aws-codepipeline-deploy-docker/


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





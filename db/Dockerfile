FROM mysql:5.7
# run create.sql on init
#ADD db/dbinit.sql /docker-entrypoint-initdb.d
#For docker compose
ADD dbinit.sql /docker-entrypoint-initdb.d

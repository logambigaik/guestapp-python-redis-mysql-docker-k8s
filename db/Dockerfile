FROM mysql:latest
ADD dbinit.sql /src/sql
ADD /src/sql /docker-entrypoint-initdb.d/

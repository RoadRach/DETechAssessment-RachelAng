FROM postgres:latest
ENV POSTGRES_USER yourusername
ENV POSTGRES_PASSWORD yourpassword
ENV POSTGRES_DB db

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432
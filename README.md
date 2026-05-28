# Docker Flask App

## What the app does

This is a simple Flask application that connects to a MySQL database.
When you visit the root route (`/`), it attempts to connect to MySQL using environment variables and returns one of two responses:

- `Hello World! Connected to MySQL successfully.` if the database connection succeeds
- `Database connection failed: <error>` if the connection cannot be established

## How to run it with Docker Compose

1. Make sure Docker and Docker Compose are installed.
2. In the project root, run:

```bash
docker compose up --build
```

3. Open your browser and go to:

```text
http://localhost
```

The Flask app is served on container port `5000`, and Docker Compose maps it to host port `80`.

## Environment variables

This project uses `env_file.env` for environment configuration. The required variables are:

- `DB_HOST` - Hostname of the MySQL service (set to `mysql` in Docker Compose)
- `DB_USER` - MySQL username
- `DB_PASSWORD` - MySQL password
- `DB_NAME` - Database name to connect to
- `MYSQL_ROOT_PASSWORD` - Root password for the MySQL container
- `MYSQL_DATABASE` - Initial MySQL database to create

Example values from `env_file.env`:

```dotenv
DB_HOST=mysql
DB_PASSWORD=root
DB_USER=root
DB_NAME=flask
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=flask
```

## Notes

- The Flask container depends on the `mysql-app` service and waits until MySQL is healthy.
- The container names are `flask` for the Flask app and `mysql` for the MySQL database.
- The app uses `requirements.txt` to install `flask` and `mysql-connector-python`.

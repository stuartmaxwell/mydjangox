# My Django X

Inspired by Will Vincent's [DjangoX project](https://github.com/wsvincent/djangox).

## Features

- Django 5.0.latest & Python 3.12.latest
- Basic first app called `website`
- Basic template with Bootstrap
- Dockerfile and docker-compose file
- Github Actions workflow to build the Docker file
- Lots of other config inspired by [Adam Johnson's Boost Your Django DX book](https://adamchainz.gumroad.com/l/byddx)

## Installation

1. Git clone this repository: `git clone ...`
2. Change directory into the repo: `cd mydjangox`
3. Create a virtual environment: e.g. `uv venv`
4. Activate the virtual environment: `source .venv/bin/activate`
5. Compile the requirements: e.g. `uv pip compile --upgrade requirements.in -o requirements.txt`
6. Install requirements: e.g. `uv pip sync requirements.txt`
7. Run the Django migrations: `python manage.py migrate`
8. Create a superuser: `python manage.py createsuperuser`
9. Start the server: `python manage.py runserver`
10. Navigate to: <http://127.0.0.1:8000>

## More Configuration

- Rename `env.template` to `.env` and configure the following settings:

  | Env Name            | Env Value                                                                                          |
  | ------------------- | -------------------------------------------------------------------------------------------------- |
  | SECRET_KEY          | The Django secret key to add to the `settings.py` file.                                            |
  | DEBUG               | Ensure this is set to `False` in production.                                                       |
  | ALLOWED_HOSTS       | List of allowed hosts, e.g. `example.com,www.example.com`.                                         |
  | EMAIL_HOST          | Name or IP address of the SMTP server.                                                             |
  | EMAIL_PORT          | The port of the SMTP server.                                                                       |
  | EMAIL_HOST_USER     | The username to authenticate with the SMTP server.                                                 |
  | EMAIL_HOST_PASSWORD | The password for the SMTP server username.                                                         |
  | EMAIL_USE_TLS       | Either `True` or `False` to use TLS.                                                               |
  | DEFAULT_FROM_EMAIL  | The email address to send emails from .                                                            |
  | DB_ENGINE           | The database engine to use.                                                                        |
  | DB_NAME             | The database name to connect to. If using SQLite, this will be the filename without the extension. |
  | DB_HOST             | Name or IP address of the database server.                                                         |
  | DB_PORT             | The port of the database server.                                                                   |
  | DB_USER             | The username to authenticate with the database server.                                             |
  | DB_PASSWORD         | The password for the database server username.                                                     |
  | WHITENOISE_STATIC   | Boolean value that turns on Whitenoise for serving static content.                                 |
  | ADMIN_URL           | The path to the Admin site so it can be hidden from easily being guessed.                          |

## Github Action

- Configure the following repository secrets:

  - `TOKEN_GITHUB`: This should be a personal access token with read and write permissions for the repo.
  - `DOCKER_WEBHOOK`: This is a webhook that will be called after the image has been created. Useful for kicking off an automation to restart and re-pull the image. If you don't want to use this, delete the `Send POST request to webhook` action from the workflow in the `docker-image.yml` file.

- Push to Github `main` branch to kick off the workflow.

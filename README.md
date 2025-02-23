# My Django X

Inspired by Will Vincent's [DjangoX project](https://github.com/wsvincent/djangox).

## Features

- Django 5.1 & Python 3.13
- Basic first app called `website`
- Basic template with Bootstrap
- Dockerfile and docker-compose file
- Lots of other config inspired by [Adam Johnson's Boost Your Django DX book](https://adamchainz.gumroad.com/l/byddx)

## Requirements

`uv` is required, and `just` is recommended to use the commands in the `justfile`.

- `uv` - `curl -LsSf https://astral.sh/uv/install.sh | sh`
- `just` - `uv tool install rust-just`

## Installation

### Recommended instructions

1. Create the directory where you want your project to live and change to that directory.
2. Then, run the following one-liner which will create a django project using the MyDjangoX template:
    `uvx --from django django-admin startproject --template https://github.com/stuartmaxwell/mydjangox/archive/refs/heads/main.zip mydjangox .`
3. Run the Django migrations: `just migrate`
4. Create a superuser: `just createsuperuser`
5. Start the server: `just run`
6. Navigate to: <http://127.0.0.1:8000>
7. Bonus: run `just test` to see if everything is working.

### Old Manual instructions

1. Download and unzip the code: `curl https://codeload.github.com/stuartmaxwell/mydjangox/zip/refs/heads/main -o mydjangox.zip`
2. Rename the directory from `mydjangox-main` to your project name
3. Change directory into the repo: `cd <your_project_name>`
4. Create a virtual environment. This will also download Python if needed: `just venv`
5. Install requirements: `just sync`
6. Optional: update requirements: `just sync-up`
7. Run the Django migrations: `just migrate`
8. Create a superuser: `just createsuperuser`
9. Start the server: `just run`
10. Navigate to: <http://127.0.0.1:8000>
11. Bonus: run `just test` to see if everything is working.

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

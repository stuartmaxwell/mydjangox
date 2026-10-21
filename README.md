# My Django X

Inspired by Will Vincent's [DjangoX project](https://github.com/wsvincent/djangox).

## Features

- Django 6.1 & Python 3.15
- Basic first app called `website`
- Basic template with Bootstrap
- Dockerfile and docker-compose file
- Backup and restore scripts for sqlite databases
- Lots of other config inspired by [Adam Johnson's Boost Your Django DX book](https://adamchainz.gumroad.com/l/byddx)

## Requirements

The following tools should be installed before starting:

- `pdm` - preferred project manager, install with `curl -sSL https://pdm-project.org/install.sh | bash`
- `django` - installing Django with `pipx install django` will put the `django-admin` binary on your path.
- `just` - used for the `justfile` commands. Can be installed with `pipx install rust-just` or with a package manager
- `dangofmt` - used for linting and can be installed with `pipx install dangofmt`
- `pre-commit` - used for the pre-commit commands and can be installed with `pipx install pre-commit`
- `ruff` - used for linting and formatting, install with `pipx install ruff`

## Installation

### Recommended instructions

1. Create the directory where you want your project to live and change to that directory.
2. Then, run the following one-liner which will create a django project using the MyDjangoX template:
    `django-admin startproject --template https://github.com/stuartmaxwell/mydjangox/archive/refs/heads/main.zip mydjangox .`
3. Run the Django migrations: `just migrate`
4. Create a superuser: `just createsuperuser`
5. Start the server: `just run`
6. Navigate to: <http://127.0.0.1:8000>
7. Bonus: run `just test` to see if everything is working.

## Configuration

- Rename `env.template` to `.env` and configure/remove the required settings.
- For local development, ensure that `DEBUG=True` has been set - this is the only one **required** for local dev.
- For production, most of the others should be set, but see the table below for details.
- If using the backup script with a Sqlite database, ensure the following are all configured:
  - `DB_NAME`
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `BACKUPS_S3_ENDPOINT`
  - `BACKUPS_S3_BUCKET`


  | Env Name              | Env Value                                                                                          |
  | ----------------------|----------------------------------------------------------------------------------------------------|
  | DEBUG                 | This is `False` by default, so set to `True` for local development.                                |
  | SECRET_KEY            | The Django secret key to add to the `settings.py` file.                                            |
  | ALLOWED_HOSTS         | List of allowed hosts, e.g. `example.com,www.example.com`.                                         |
  | EMAIL_HOST            | Name or IP address of the SMTP server.                                                             |
  | EMAIL_PORT            | The port of the SMTP server.                                                                       |
  | EMAIL_HOST_USER       | The username to authenticate with the SMTP server.                                                 |
  | EMAIL_HOST_PASSWORD   | The password for the SMTP server username.                                                         |
  | EMAIL_USE_TLS         | Either `True` or `False` to use TLS.                                                               |
  | DEFAULT_FROM_EMAIL    | The email address to send emails from .                                                            |
  | DB_ENGINE             | The database engine to use.                                                                        |
  | DB_NAME               | The database name to connect to. If using SQLite, this will be the filename without the extension. |
  | DB_HOST               | Name or IP address of the database server.                                                         |
  | DB_PORT               | The port of the database server.                                                                   |
  | DB_USER               | The username to authenticate with the database server.                                             |
  | DB_PASSWORD           | The password for the database server username.                                                     |
  | WHITENOISE_STATIC     | Boolean value that turns on Whitenoise for serving static content.                                 |
  | ADMIN_URL             | The path to the Admin site so it can be hidden from easily being guessed.                          |
  | AWS_ACCESS_KEY_ID     | Only required if backing up the sqlite database to a remote S3 bucket.                             |
  | AWS_SECRET_ACCESS_KEY | Only required if backing up the sqlite database to a remote S3 bucket.                             |
  | BACKUPS_S3_ENDPOINT   | Only required for backups. Should point to an S3 URL.                                              |
  | BACKUPS_S3_BUCKET     | Only required for backups. The name of the S3 bucket that will be appended to the S3 URL.          |

# My Django X

Inspired by Will Vincent's [DjangoX project](https://github.com/wsvincent/djangox).

## Features

- Django 6.0 & Python 3.14
- Basic first app called `website`
- Basic template with Bootstrap
- Dockerfile and docker-compose file
- Lots of other config inspired by [Adam Johnson's Boost Your Django DX book](https://adamchainz.gumroad.com/l/byddx)

## Requirements

The following tools should be installed before starting:

- `pdm` - preferred project manager, install with `curl -sSL https://pdm-project.org/install.sh | bash`
- `django` - installing Django with `pipx install django` will put the `django-admin` binary on your path.
- `just` - used for the `justfile` commands. Can be installed with `pipx install rust-just` or with a package manager
- `djlint` - used for linting and can be installed with `pipx install djlint`
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

## More Configuration

- Rename `env.template` to `.env` and configure the following settings, or just copy the ones you need into a new .env file.

  | Env Name            | Env Value                                                                                          |
  | ------------------- | -------------------------------------------------------------------------------------------------- |
  | DEBUG               | This is `False` by default, so set to `True` for local development.                                |
  | SECRET_KEY          | The Django secret key to add to the `settings.py` file.                                            |
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

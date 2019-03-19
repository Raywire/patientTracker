[![Build Status](https://travis-ci.org/Raywire/patientTracker.svg?branch=develop)](https://travis-ci.org/Raywire/patientTracker)
[![Coverage Status](https://coveralls.io/repos/github/Raywire/patientTracker/badge.svg?branch=develop)](https://coveralls.io/github/Raywire/patientTracker?branch=develop)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/57a5176fa85f42a7be59cf53dc0d1a4c)](https://www.codacy.com/app/Raywire/patientTracker?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Raywire/patientTracker&amp;utm_campaign=Badge_Grade)

**Project**: Patient Tracker

**Description**: Patient Tracker is a system for hospitals to manage records of all their patients in one centralised database.

## Getting Started

git clone the repo

### Prerequisites

A postgres database is required for development
Install pipenv using Homebrew, Linuxbrew or pip
```shell
brew install pipenv
```

**Setting up the database with a user who has all privileges**
```sql
sudo -u postgres psql
postgres=# create database your_database;
postgres=# create user your_username with encrypted password 'your_password';
postgres=# grant all privileges on database your_database to your_username;
```
### Contents of .env file

```python
DEBUG=True
SECRET_KEY='your-secret-key-here'
DATABASE_URL=psql://user:password@127.0.0.1:5432/database_name
```
## Running the app
cd into the patienttracker folder
```python
cd patienttracker/
```

Run the command to install all requirements from Pipfile.lock
```python
pipenv install
```

To activate the virtual environment run the command below
```python
pipenv shell
```

Run the application by starting the server
```python
python manage.py runserver
```

## Running the tests

```python
cd patienttracker/
python manage.py test
```
In case you do not have permission to create a database run the following command on psql
```sql
sudo -u postgres psql
ALTER ROLE your_username CREATEDB;
```

Running tests with coverage
```python
cd patienttracker/
coverage run --source="." manage.py test
coverage report
```

## Built With

*   [Django Rest Framework](https://www.django-rest-framework.org/) - Django

## API Endpoints
```shell
POST /api/v1/patients

GET /api/v1/patients

GET /api/v1/patients/<id>

PUT /api/v1/patients/<id>

DELETE /api/v1/patients<id>
```
## Author

*   **Ryan Simiyu** 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
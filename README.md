# API Books

## Description

## Usage

### Pre-requisites

- Python >=3
- Postgres >=14
- Venv

### Installation

- Create database

```shell
sh create_database.sh
```

- Install dependencies

```shell
pip install -r requirements.txt 
```

- Create migrations

```shell
python manage.py makemigrations
```

- Run migrations

```shell
python manage.py migrate
```

### Run server

```shell
python manage.py runserver
```


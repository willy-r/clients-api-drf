# Clients API - Django Rest Framework

A clients REST API made with some intermediaries concepts of Django Rest Framework.

Concepts applied her:

- Validating
- Filters
- Searching


## Endpoints

| Method | Route | Description |
| ------ | ----- | ----------- |
| **GET** | `/clients` | Gets all clients |
| **GET** | `/clients/{id}` | Gets the client by {id} |
| **POST** | `/clients` | Creates a new client |
| **PATCH/PUT** | `/clients/{id}` | Updates the client by {id} |
| **DELETE** | `/clients/{id}` | Deletes the client by {id} |


## Running locally

You need to have **Python 3.7.4+**

Define the following envs:

`SECRET_KEY` - The SECRET KEY for your Django project

Clone this repo and go to project root directory:

```bash
$ git clone https://github.com/willy-r/clients-api-drf.git
$ cd clients-api-drf
```

Create virtual enviroment and activate it:

```bash
$ python -m venv venv
$ source venv/bin/activate
```

Install dependencies:

```bash
$ (venv) pip install -r requirements.txt
```

Migrate database, create superuser and start server:

```bash
$ (venv) python manage.py migrate
$ (venv) python manage.py createsuperuser
$ ...
$ (venv) python manage.py runserver
```

Access API:

[`http://localhost:8000`](http://localhost:8000)


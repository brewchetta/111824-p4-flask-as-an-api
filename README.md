# REST APIs with Flask

## Learning Goals

- Recap on building models / migrating databases

- Retrieving database data with a GET request

- Creating new data with a POST request

- Updating data with a PATCH request

- Deleting data with a DELETE request

## Getting Started

Begin with:

```
pipenv install
pipenv shell
cd server

BUILD YOUR MODEL(S)

flask db init
flask db migrate -m "initialize database"
flask db upgrade
```
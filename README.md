# Learn VueJS Project

## Backend

### Tech:
Postgres, SQLAlchemy, FastAPI.

### Setup
* First create venv using comand ``` python3.11 -m venv ../  ``` from project directory
* Activate venv via ```source /bin/activate```
* Install requirements ```pip install -r requirements.txt```
* Run backend using gunicorn 

```sh -c "gunicorn --bind :8000  main:app -k uvicorn.workers.UvicornWorker --preload"```

-----------

## Frontend

### Tech:
VueJS, Axios, VueRouter.

### Setup
* Go to frontend directory ```cd frontend```
* Run ```npm run install``` for install node modules
* Run ```npm run build``` for collect data for prod
* Run ```npm run serve``` for run server

---------------------------------------


Backend: http://0.0.0.0:8000

OpenAPI: http://0.0.0.0:8000/api/openapi

Frontend: http://127.0.0.1:8080
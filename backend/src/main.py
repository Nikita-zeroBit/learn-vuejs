from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from api.v1.users import router as users_router
from api.v1.books import router as books_router
from db import database
from db.database import Base, SessionLocal, engine


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Web API',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
    description='The web api',
    version='1.0.0'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8080", "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.on_event('startup')
def startup():
    database.db_connector = SessionLocal()


@app.on_event('shutdown')
def shutdown():
    database.db_connector.close()


app.include_router(users_router, prefix='/api/users', tags=['Users'])
app.include_router(books_router, prefix='/api/books', tags=['Books'])

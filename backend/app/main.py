from fastapi import FastAPI
from app.database import engine, Base
from app.routes.book_routes import router as book_router

app = FastAPI(title="Library Management System API")

Base.metadata.create_all(bind=engine)

app.include_router(book_router)

@app.get("/")
def root():
    return {"message": "Library Management System API Running"}
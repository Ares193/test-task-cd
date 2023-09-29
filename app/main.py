import uvicorn

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.main import main_router
from app.common.config import settings

app = FastAPI(
    title="Тестовое задание для компании Страна Development",
    version='0.0.1',
    contact={
        "name": "Maxim Araslanov",
        "email": "ares193@gmail.com"
    },
    root_path=settings.API_BASE_URL
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# REST API
app.include_router(main_router)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_config=None
    )

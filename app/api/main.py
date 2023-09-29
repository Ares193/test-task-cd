from fastapi import APIRouter, Request
from starlette.responses import RedirectResponse
from app.api.metrics import router as metrics_router
from app.common.config import settings

main_router = APIRouter()


@main_router.get('/', include_in_schema=False)
def main_page():
    return RedirectResponse(f"{str(settings.API_BASE_URL)}/docs")


main_router.include_router(metrics_router)

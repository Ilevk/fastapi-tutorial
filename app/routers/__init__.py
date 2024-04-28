from fastapi import APIRouter

from app.routers import class_
from app.routers import user

router = APIRouter(prefix="/v1")

router.include_router(class_.router, prefix="/class", tags=["class"])
router.include_router(user.router, prefix="/user", tags=["user"])

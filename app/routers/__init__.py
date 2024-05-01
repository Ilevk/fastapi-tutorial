from fastapi import APIRouter, Depends

from app.routers import class_
from app.routers import user
from app.core.auth import validate_api_key

router = APIRouter(prefix="/v1", dependencies=[Depends(validate_api_key)])

router.include_router(class_.router, prefix="/class", tags=["class"])
router.include_router(user.router, prefix="/user", tags=["user"])

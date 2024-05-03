from typing import Optional

from fastapi import Header

from app.core.errors import error


async def validate_api_key(api_key: Optional[str] = Header(None, alias="x-api-key")):
    if api_key is None or api_key != "{API key}":
        raise error.InvalidAPIKey()

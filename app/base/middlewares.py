from typing import Callable

from fastapi import Request

from ..db import create_engine


async def dbsession_middleware(request: Request, call_next: Callable):
    """
    Set sqlalchemy Session on every incoming request: Request
    """
    request.state.dbsession = create_engine()
    return await call_next(request)

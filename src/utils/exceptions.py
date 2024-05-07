from fastapi import Request, status
from fastapi.responses import JSONResponse


class DuplicateRecord(Exception):
    def __init__(self, detail):
        self.detail = detail


class NotFoundRecord(Exception):
    def __init__(self, detail):
        self.detail = detail


class Unauthorized(Exception):
    def __init__(self, detail):
        self.detail = detail


class Forbidden(Exception):
    def __init__(self, detail):
        self.detail = detail


async def duplicate_record_exception_handler(request: Request, exc: DuplicateRecord):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "type": "duplicate_record",
            "title": "Duplicate Record",
            "detail": exc.detail,
            "status": status.HTTP_409_CONFLICT,
        },
    )


async def not_found_exception_handler(request: Request, exc: NotFoundRecord):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "type": "not_found",
            "title": "Not Found",
            "detail": exc.detail,
            "status": status.HTTP_404_NOT_FOUND,
        },
    )


async def unauthorized_exception_handler(request: Request, exc: Unauthorized):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={
            "type": "unauthorized",
            "title": "Unauthorized",
            "detail": exc.detail,
            "status": status.HTTP_401_UNAUTHORIZED,
        },
    )


async def forbidden_exception_handler(request: Request, exc: Forbidden):
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={
            "type": "forbidden",
            "title": "Forbidden",
            "detail": exc.detail,
            "status": status.HTTP_403_FORBIDDEN,
        },
    )

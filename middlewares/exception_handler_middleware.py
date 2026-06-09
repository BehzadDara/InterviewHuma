from fastapi import Request, status
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse
from exceptions.log_exception import AppException

class ExceptionHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except AppException as e:
            return JSONResponse(status_code=e.status_code, content={'message': e.message})
        except Exception as e:
            return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={'message': str(e)})


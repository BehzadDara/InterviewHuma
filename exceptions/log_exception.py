from fastapi import status

class AppException(Exception):
    def __init__(self, message:str, status_code:int=status.HTTP_500_INTERNAL_SERVER_ERROR):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

class RateLimitException(Exception):
    def __init__(self, message:str):
        super().__init__(message, status.HTTP_429_TOO_MANY_REQUESTS)
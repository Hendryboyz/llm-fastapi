from typing import Any, Union

from ..exceptions.app_exception import AppException

class DenyFormatException(AppException):
    def __init__(
        self,
        error_code: int,
        error_message: str,
        error: Union[Any, None] = None,
        status_code: int = 422
    ):
        super().__init__(
            error_code=error_code,
            error_message=error_message,
            error=error,
            status_code=status_code
        )

class FailGenerateException(AppException):
    def __init__(
        self,
        error_code: int,
        error_message: str,
        error: Union[Any, None] = None,
        status_code: int = 500
    ):
        super().__init__(
            error_code=error_code,
            error_message=error_message,
            error=error,
            status_code=status_code
        )
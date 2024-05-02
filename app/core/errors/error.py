ERROR_400_CLASS_NOT_FOUND = "40000"
ERROR_400_CLASS_NOTICE_NOT_FOUND = "40001"
ERROR_400_CLASS_CREATION_FAILED = "40002"
ERROR_400_CLASS_NOTICE_CREATION_FAILED = "40003"
ERROR_400_CLASS_NOTICE_UPDATE_FAILED = "40004"
ERROR_400_CLASS_NOTICE_DELETE_FAILED = "40005"

ERROR_401_INVALID_API_KEY = "40100"


class BaseAPIException(Exception):
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message


class BaseAuthException(Exception):
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message


class ClassNotFoundException(BaseAPIException):
    def __init__(self):
        super().__init__(code=ERROR_400_CLASS_NOT_FOUND, message="Class not found")


class ClassCreationFailed(BaseAPIException):
    def __init__(self):
        super().__init__(
            code=ERROR_400_CLASS_CREATION_FAILED, message="Class creation failed"
        )


class ClassNoticeNotFound(BaseAPIException):
    def __init__(self):
        super().__init__(
            code=ERROR_400_CLASS_NOTICE_NOT_FOUND, message="Class Notice not found"
        )


class ClassNoticeCreationFailed(BaseAPIException):
    def __init__(self):
        super().__init__(
            code=ERROR_400_CLASS_NOTICE_CREATION_FAILED,
            message="Class Notice creation failed",
        )


class ClassNoticeUpdateFailed(BaseAPIException):
    def __init__(self):
        super().__init__(
            code=ERROR_400_CLASS_NOTICE_UPDATE_FAILED,
            message="Class Notice update failed",
        )


class ClassNoticeDeleteFailed(BaseAPIException):
    def __init__(self):
        super().__init__(
            code=ERROR_400_CLASS_NOTICE_DELETE_FAILED,
            message="Class Notice delete failed",
        )


class InvalidAPIKey(BaseAuthException):
    def __init__(self):
        super().__init__(code=ERROR_401_INVALID_API_KEY, message="Invalid API Key")

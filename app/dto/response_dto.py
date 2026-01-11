from typing import Any, Optional
from pydantic import BaseModel

class ResponseDto(BaseModel):
    code: int
    msg: str
    data: Optional[Any] = None
    count: int = 0

def success(data: Any = None) -> ResponseDto:
    return ResponseDto(code=0, msg="SUCCESS", data=data, count=0)

def success_message(msg: str, data: Any = None) -> ResponseDto:
    return ResponseDto(code=0, msg=msg, data=data, count=0)

def success_count(data: Any, count: int) -> ResponseDto:
    return ResponseDto(code=0, msg="SUCCESS", data=data, count=count)

def fail(msg: str) -> ResponseDto:
    return ResponseDto(code=1, msg=msg)

def fail_code(code: int) -> ResponseDto:
    return ResponseDto(code=code, msg="No Permission")

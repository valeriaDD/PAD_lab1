from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceInfo(_message.Message):
    __slots__ = ["service_name", "host", "port"]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    service_name: str
    host: str
    port: int
    def __init__(self, service_name: _Optional[str] = ..., host: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class ServiceRequest(_message.Message):
    __slots__ = ["service_name"]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    service_name: str
    def __init__(self, service_name: _Optional[str] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class HealthStatus(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...

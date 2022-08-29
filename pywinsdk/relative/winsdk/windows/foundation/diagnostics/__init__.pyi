# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.6

import enum
import datetime
import sys
import types
import typing

from ....  import _winrt as _winrt
from ...  import foundation
from ...  import storage

class CausalityRelation(enum.IntEnum):
    ASSIGN_DELEGATE = 0
    JOIN = 1
    CHOICE = 2
    CANCEL = 3
    ERROR = 4

class CausalitySource(enum.IntEnum):
    APPLICATION = 0
    LIBRARY = 1
    SYSTEM = 2

class CausalitySynchronousWork(enum.IntEnum):
    COMPLETION_NOTIFICATION = 0
    PROGRESS_NOTIFICATION = 1
    EXECUTION = 2

class CausalityTraceLevel(enum.IntEnum):
    REQUIRED = 0
    IMPORTANT = 1
    VERBOSE = 2

class ErrorOptions(enum.IntFlag):
    NONE = 0
    SUPPRESS_EXCEPTIONS = 0x1
    FORCE_EXCEPTIONS = 0x2
    USE_SET_ERROR_INFO = 0x4
    SUPPRESS_SET_ERROR_INFO = 0x8

class LoggingFieldFormat(enum.IntEnum):
    DEFAULT = 0
    HIDDEN = 1
    STRING = 2
    BOOLEAN = 3
    HEXADECIMAL = 4
    PROCESS_ID = 5
    THREAD_ID = 6
    PORT = 7
    IPV4_ADDRESS = 8
    IPV6_ADDRESS = 9
    SOCKET_ADDRESS = 10
    XML = 11
    JSON = 12
    WIN32_ERROR = 13
    N_T_STATUS = 14
    H_RESULT = 15
    FILE_TIME = 16
    SIGNED = 17
    UNSIGNED = 18

class LoggingLevel(enum.IntEnum):
    VERBOSE = 0
    INFORMATION = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4

class LoggingOpcode(enum.IntEnum):
    INFO = 0
    START = 1
    STOP = 2
    REPLY = 6
    RESUME = 7
    SUSPEND = 8
    SEND = 9

Self = typing.TypeVar('Self')

class AsyncCausalityTracer(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> AsyncCausalityTracer: ...
    @staticmethod
    def trace_operation_completion(trace_level: CausalityTraceLevel, source: CausalitySource, platform_id: _winrt.Guid, operation_id: _winrt.UInt64, status: winsdk.windows.foundation.AsyncStatus) -> None: ...
    @staticmethod
    def trace_operation_creation(trace_level: CausalityTraceLevel, source: CausalitySource, platform_id: _winrt.Guid, operation_id: _winrt.UInt64, operation_name: str, related_context: _winrt.UInt64) -> None: ...
    @staticmethod
    def trace_operation_relation(trace_level: CausalityTraceLevel, source: CausalitySource, platform_id: _winrt.Guid, operation_id: _winrt.UInt64, relation: CausalityRelation) -> None: ...
    @staticmethod
    def trace_synchronous_work_completion(trace_level: CausalityTraceLevel, source: CausalitySource, work: CausalitySynchronousWork) -> None: ...
    @staticmethod
    def trace_synchronous_work_start(trace_level: CausalityTraceLevel, source: CausalitySource, platform_id: _winrt.Guid, operation_id: _winrt.UInt64, work: CausalitySynchronousWork) -> None: ...
    @staticmethod
    def add_tracing_status_changed(handler: winsdk.windows.foundation.EventHandler[TracingStatusChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @staticmethod
    def remove_tracing_status_changed(cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class ErrorDetails(_winrt.Object):
    description: str
    help_uri: typing.Optional[winsdk.windows.foundation.Uri]
    long_description: str
    @staticmethod
    def _from(obj: _winrt.Object) -> ErrorDetails: ...
    @staticmethod
    def create_from_h_result_async(error_code: _winrt.Int32) -> winsdk.windows.foundation.IAsyncOperation[ErrorDetails]: ...

class FileLoggingSession(_winrt.Object):
    name: str
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> FileLoggingSession: ...
    def __new__(cls: typing.Type[FileLoggingSession], name: str) -> FileLoggingSession:...
    @typing.overload
    def add_logging_channel(self, logging_channel: typing.Optional[ILoggingChannel]) -> None: ...
    @typing.overload
    def add_logging_channel(self, logging_channel: typing.Optional[ILoggingChannel], max_level: LoggingLevel) -> None: ...
    def close(self) -> None: ...
    def close_and_save_to_file_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFile]: ...
    def remove_logging_channel(self, logging_channel: typing.Optional[ILoggingChannel]) -> None: ...
    def add_log_file_generated(self, handler: winsdk.windows.foundation.TypedEventHandler[IFileLoggingSession, LogFileGeneratedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_log_file_generated(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class LogFileGeneratedEventArgs(_winrt.Object):
    file: typing.Optional[winsdk.windows.storage.StorageFile]
    @staticmethod
    def _from(obj: _winrt.Object) -> LogFileGeneratedEventArgs: ...

class LoggingActivity(_winrt.Object):
    id: _winrt.Guid
    name: str
    channel: typing.Optional[LoggingChannel]
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> LoggingActivity: ...
    @typing.overload
    def __new__(cls: typing.Type[LoggingActivity], activity_name: str, logging_channel: typing.Optional[ILoggingChannel]) -> LoggingActivity:...
    @typing.overload
    def __new__(cls: typing.Type[LoggingActivity], activity_name: str, logging_channel: typing.Optional[ILoggingChannel], level: LoggingLevel) -> LoggingActivity:...
    def close(self) -> None: ...
    @typing.overload
    def is_enabled(self) -> _winrt.Boolean: ...
    @typing.overload
    def is_enabled(self, level: LoggingLevel) -> _winrt.Boolean: ...
    @typing.overload
    def is_enabled(self, level: LoggingLevel, keywords: _winrt.Int64) -> _winrt.Boolean: ...
    @typing.overload
    def log_event(self, event_name: str) -> None: ...
    @typing.overload
    def log_event(self, event_name: str, fields: typing.Optional[LoggingFields]) -> None: ...
    @typing.overload
    def log_event(self, event_name: str, fields: typing.Optional[LoggingFields], level: LoggingLevel) -> None: ...
    @typing.overload
    def log_event(self, event_name: str, fields: typing.Optional[LoggingFields], level: LoggingLevel, options: typing.Optional[LoggingOptions]) -> None: ...
    @typing.overload
    def start_activity(self, start_event_name: str) -> typing.Optional[LoggingActivity]: ...
    @typing.overload
    def start_activity(self, start_event_name: str, fields: typing.Optional[LoggingFields]) -> typing.Optional[LoggingActivity]: ...
    @typing.overload
    def start_activity(self, start_event_name: str, fields: typing.Optional[LoggingFields], level: LoggingLevel) -> typing.Optional[LoggingActivity]: ...
    @typing.overload
    def start_activity(self, start_event_name: str, fields: typing.Optional[LoggingFields], level: LoggingLevel, options: typing.Optional[LoggingOptions]) -> typing.Optional[LoggingActivity]: ...
    @typing.overload
    def stop_activity(self, stop_event_name: str) -> None: ...
    @typing.overload
    def stop_activity(self, stop_event_name: str, fields: typing.Optional[LoggingFields]) -> None: ...
    @typing.overload
    def stop_activity(self, stop_event_name: str, fields: typing.Optional[LoggingFields], options: typing.Optional[LoggingOptions]) -> None: ...

class LoggingChannel(_winrt.Object):
    enabled: _winrt.Boolean
    level: LoggingLevel
    name: str
    id: _winrt.Guid
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> LoggingChannel: ...
    @typing.overload
    def __new__(cls: typing.Type[LoggingChannel], name: str, options: typing.Optional[LoggingChannelOptions]) -> LoggingChannel:...
    @typing.overload
    def __new__(cls: typing.Type[LoggingChannel], name: str, options: typing.Optional[LoggingChannelOptions], id: _winrt.Guid) -> LoggingChannel:...
    @typing.overload
    def __new__(cls: typing.Type[LoggingChannel], name: str) -> LoggingChannel:...
    def close(self) -> None: ...
    @typing.overload
    def is_enabled(self) -> _winrt.Boolean: ...
    @typing.overload
    def is_enabled(self, level: LoggingLevel) -> _winrt.Boolean: ...
    @typing.overload
    def is_enabled(self, level: LoggingLevel, keywords: _winrt.Int64) -> _winrt.Boolean: ...
    @typing.overload
    def log_event(self, event_name: str) -> None: ...
    @typing.overload
    def log_event(self, event_name: str, fields: typing.Optional[LoggingFields]) -> None: ...
    @typing.overload
    def log_event(self, event_name: str, fields: typing.Optional[LoggingFields], level: LoggingLevel) -> None: ...
    @typing.overload
    def log_event(self, event_name: str, fields: typing.Optional[LoggingFields], level: LoggingLevel, options: typing.Optional[LoggingOptions]) -> None: ...
    @typing.overload
    def log_message(self, event_string: str) -> None: ...
    @typing.overload
    def log_message(self, event_string: str, level: LoggingLevel) -> None: ...
    @typing.overload
    def log_value_pair(self, value1: str, value2: _winrt.Int32) -> None: ...
    @typing.overload
    def log_value_pair(self, value1: str, value2: _winrt.Int32, level: LoggingLevel) -> None: ...
    @typing.overload
    def start_activity(self, start_event_name: str) -> typing.Optional[LoggingActivity]: ...
    @typing.overload
    def start_activity(self, start_event_name: str, fields: typing.Optional[LoggingFields]) -> typing.Optional[LoggingActivity]: ...
    @typing.overload
    def start_activity(self, start_event_name: str, fields: typing.Optional[LoggingFields], level: LoggingLevel) -> typing.Optional[LoggingActivity]: ...
    @typing.overload
    def start_activity(self, start_event_name: str, fields: typing.Optional[LoggingFields], level: LoggingLevel, options: typing.Optional[LoggingOptions]) -> typing.Optional[LoggingActivity]: ...
    def add_logging_enabled(self, handler: winsdk.windows.foundation.TypedEventHandler[ILoggingChannel, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_logging_enabled(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class LoggingChannelOptions(_winrt.Object):
    group: _winrt.Guid
    @staticmethod
    def _from(obj: _winrt.Object) -> LoggingChannelOptions: ...
    @typing.overload
    def __new__(cls: typing.Type[LoggingChannelOptions]) -> LoggingChannelOptions:...
    @typing.overload
    def __new__(cls: typing.Type[LoggingChannelOptions], group: _winrt.Guid) -> LoggingChannelOptions:...

class LoggingFields(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> LoggingFields: ...
    def __new__(cls: typing.Type[LoggingFields]) -> LoggingFields:...
    @typing.overload
    def add_boolean(self, name: str, value: _winrt.Boolean) -> None: ...
    @typing.overload
    def add_boolean(self, name: str, value: _winrt.Boolean, format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_boolean(self, name: str, value: _winrt.Boolean, format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_boolean_array(self, name: str, value: typing.Sequence[_winrt.Boolean]) -> None: ...
    @typing.overload
    def add_boolean_array(self, name: str, value: typing.Sequence[_winrt.Boolean], format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_boolean_array(self, name: str, value: typing.Sequence[_winrt.Boolean], format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_char16(self, name: str, value: _winrt.Char16) -> None: ...
    @typing.overload
    def add_char16(self, name: str, value: _winrt.Char16, format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_char16(self, name: str, value: _winrt.Char16, format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_char16_array(self, name: str, value: typing.Sequence[_winrt.Char16]) -> None: ...
    @typing.overload
    def add_char16_array(self, name: str, value: typing.Sequence[_winrt.Char16], format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_char16_array(self, name: str, value: typing.Sequence[_winrt.Char16], format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_date_time(self, name: str, value: datetime.datetime) -> None: ...
    @typing.overload
    def add_date_time(self, name: str, value: datetime.datetime, format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_date_time(self, name: str, value: datetime.datetime, format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_date_time_array(self, name: str, value: typing.Sequence[datetime.datetime]) -> None: ...
    @typing.overload
    def add_date_time_array(self, name: str, value: typing.Sequence[datetime.datetime], format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_date_time_array(self, name: str, value: typing.Sequence[datetime.datetime], format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_double(self, name: str, value: _winrt.Double) -> None: ...
    @typing.overload
    def add_double(self, name: str, value: _winrt.Double, format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_double(self, name: str, value: _winrt.Double, format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_double_array(self, name: str, value: typing.Sequence[_winrt.Double]) -> None: ...
    @typing.overload
    def add_double_array(self, name: str, value: typing.Sequence[_winrt.Double], format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_double_array(self, name: str, value: typing.Sequence[_winrt.Double], format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_empty(self, name: str) -> None: ...
    @typing.overload
    def add_empty(self, name: str, format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_empty(self, name: str, format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_guid(self, name: str, value: _winrt.Guid) -> None: ...
    @typing.overload
    def add_guid(self, name: str, value: _winrt.Guid, format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_guid(self, name: str, value: _winrt.Guid, format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_guid_array(self, name: str, value: typing.Sequence[_winrt.Guid]) -> None: ...
    @typing.overload
    def add_guid_array(self, name: str, value: typing.Sequence[_winrt.Guid], format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_guid_array(self, name: str, value: typing.Sequence[_winrt.Guid], format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_int16(self, name: str, value: _winrt.Int16) -> None: ...
    @typing.overload
    def add_int16(self, name: str, value: _winrt.Int16, format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_int16(self, name: str, value: _winrt.Int16, format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_int16_array(self, name: str, value: typing.Sequence[_winrt.Int16]) -> None: ...
    @typing.overload
    def add_int16_array(self, name: str, value: typing.Sequence[_winrt.Int16], format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_int16_array(self, name: str, value: typing.Sequence[_winrt.Int16], format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_int32(self, name: str, value: _winrt.Int32) -> None: ...
    @typing.overload
    def add_int32(self, name: str, value: _winrt.Int32, format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_int32(self, name: str, value: _winrt.Int32, format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_int32_array(self, name: str, value: typing.Sequence[_winrt.Int32]) -> None: ...
    @typing.overload
    def add_int32_array(self, name: str, value: typing.Sequence[_winrt.Int32], format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_int32_array(self, name: str, value: typing.Sequence[_winrt.Int32], format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_int64(self, name: str, value: _winrt.Int64) -> None: ...
    @typing.overload
    def add_int64(self, name: str, value: _winrt.Int64, format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_int64(self, name: str, value: _winrt.Int64, format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_int64_array(self, name: str, value: typing.Sequence[_winrt.Int64]) -> None: ...
    @typing.overload
    def add_int64_array(self, name: str, value: typing.Sequence[_winrt.Int64], format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_int64_array(self, name: str, value: typing.Sequence[_winrt.Int64], format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_point(self, name: str, value: winsdk.windows.foundation.Point) -> None: ...
    @typing.overload
    def add_point(self, name: str, value: winsdk.windows.foundation.Point, format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_point(self, name: str, value: winsdk.windows.foundation.Point, format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_point_array(self, name: str, value: typing.Sequence[winsdk.windows.foundation.Point]) -> None: ...
    @typing.overload
    def add_point_array(self, name: str, value: typing.Sequence[winsdk.windows.foundation.Point], format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_point_array(self, name: str, value: typing.Sequence[winsdk.windows.foundation.Point], format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_rect(self, name: str, value: winsdk.windows.foundation.Rect) -> None: ...
    @typing.overload
    def add_rect(self, name: str, value: winsdk.windows.foundation.Rect, format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_rect(self, name: str, value: winsdk.windows.foundation.Rect, format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_rect_array(self, name: str, value: typing.Sequence[winsdk.windows.foundation.Rect]) -> None: ...
    @typing.overload
    def add_rect_array(self, name: str, value: typing.Sequence[winsdk.windows.foundation.Rect], format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_rect_array(self, name: str, value: typing.Sequence[winsdk.windows.foundation.Rect], format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_single(self, name: str, value: _winrt.Single) -> None: ...
    @typing.overload
    def add_single(self, name: str, value: _winrt.Single, format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_single(self, name: str, value: _winrt.Single, format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_single_array(self, name: str, value: typing.Sequence[_winrt.Single]) -> None: ...
    @typing.overload
    def add_single_array(self, name: str, value: typing.Sequence[_winrt.Single], format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_single_array(self, name: str, value: typing.Sequence[_winrt.Single], format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_size(self, name: str, value: winsdk.windows.foundation.Size) -> None: ...
    @typing.overload
    def add_size(self, name: str, value: winsdk.windows.foundation.Size, format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_size(self, name: str, value: winsdk.windows.foundation.Size, format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_size_array(self, name: str, value: typing.Sequence[winsdk.windows.foundation.Size]) -> None: ...
    @typing.overload
    def add_size_array(self, name: str, value: typing.Sequence[winsdk.windows.foundation.Size], format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_size_array(self, name: str, value: typing.Sequence[winsdk.windows.foundation.Size], format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_string(self, name: str, value: str) -> None: ...
    @typing.overload
    def add_string(self, name: str, value: str, format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_string(self, name: str, value: str, format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_string_array(self, name: str, value: typing.Sequence[str]) -> None: ...
    @typing.overload
    def add_string_array(self, name: str, value: typing.Sequence[str], format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_string_array(self, name: str, value: typing.Sequence[str], format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_time_span(self, name: str, value: datetime.timedelta) -> None: ...
    @typing.overload
    def add_time_span(self, name: str, value: datetime.timedelta, format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_time_span(self, name: str, value: datetime.timedelta, format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_time_span_array(self, name: str, value: typing.Sequence[datetime.timedelta]) -> None: ...
    @typing.overload
    def add_time_span_array(self, name: str, value: typing.Sequence[datetime.timedelta], format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_time_span_array(self, name: str, value: typing.Sequence[datetime.timedelta], format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_uint16(self, name: str, value: _winrt.UInt16) -> None: ...
    @typing.overload
    def add_uint16(self, name: str, value: _winrt.UInt16, format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_uint16(self, name: str, value: _winrt.UInt16, format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_uint16_array(self, name: str, value: typing.Sequence[_winrt.UInt16]) -> None: ...
    @typing.overload
    def add_uint16_array(self, name: str, value: typing.Sequence[_winrt.UInt16], format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_uint16_array(self, name: str, value: typing.Sequence[_winrt.UInt16], format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_uint32(self, name: str, value: _winrt.UInt32) -> None: ...
    @typing.overload
    def add_uint32(self, name: str, value: _winrt.UInt32, format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_uint32(self, name: str, value: _winrt.UInt32, format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_uint32_array(self, name: str, value: typing.Sequence[_winrt.UInt32]) -> None: ...
    @typing.overload
    def add_uint32_array(self, name: str, value: typing.Sequence[_winrt.UInt32], format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_uint32_array(self, name: str, value: typing.Sequence[_winrt.UInt32], format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_uint64(self, name: str, value: _winrt.UInt64) -> None: ...
    @typing.overload
    def add_uint64(self, name: str, value: _winrt.UInt64, format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_uint64(self, name: str, value: _winrt.UInt64, format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_uint64_array(self, name: str, value: typing.Sequence[_winrt.UInt64]) -> None: ...
    @typing.overload
    def add_uint64_array(self, name: str, value: typing.Sequence[_winrt.UInt64], format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_uint64_array(self, name: str, value: typing.Sequence[_winrt.UInt64], format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_uint8(self, name: str, value: _winrt.UInt8) -> None: ...
    @typing.overload
    def add_uint8(self, name: str, value: _winrt.UInt8, format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_uint8(self, name: str, value: _winrt.UInt8, format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def add_uint8_array(self, name: str, value: typing.Sequence[_winrt.UInt8]) -> None: ...
    @typing.overload
    def add_uint8_array(self, name: str, value: typing.Sequence[_winrt.UInt8], format: LoggingFieldFormat) -> None: ...
    @typing.overload
    def add_uint8_array(self, name: str, value: typing.Sequence[_winrt.UInt8], format: LoggingFieldFormat, tags: _winrt.Int32) -> None: ...
    @typing.overload
    def begin_struct(self, name: str) -> None: ...
    @typing.overload
    def begin_struct(self, name: str, tags: _winrt.Int32) -> None: ...
    def clear(self) -> None: ...
    def end_struct(self) -> None: ...

class LoggingOptions(_winrt.Object):
    task: _winrt.Int16
    tags: _winrt.Int32
    related_activity_id: _winrt.Guid
    opcode: LoggingOpcode
    keywords: _winrt.Int64
    activity_id: _winrt.Guid
    @staticmethod
    def _from(obj: _winrt.Object) -> LoggingOptions: ...
    @typing.overload
    def __new__(cls: typing.Type[LoggingOptions]) -> LoggingOptions:...
    @typing.overload
    def __new__(cls: typing.Type[LoggingOptions], keywords: _winrt.Int64) -> LoggingOptions:...

class LoggingSession(_winrt.Object):
    name: str
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> LoggingSession: ...
    def __new__(cls: typing.Type[LoggingSession], name: str) -> LoggingSession:...
    @typing.overload
    def add_logging_channel(self, logging_channel: typing.Optional[ILoggingChannel]) -> None: ...
    @typing.overload
    def add_logging_channel(self, logging_channel: typing.Optional[ILoggingChannel], max_level: LoggingLevel) -> None: ...
    def close(self) -> None: ...
    def remove_logging_channel(self, logging_channel: typing.Optional[ILoggingChannel]) -> None: ...
    def save_to_file_async(self, folder: typing.Optional[winsdk.windows.storage.IStorageFolder], file_name: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFile]: ...

class RuntimeBrokerErrorSettings(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> RuntimeBrokerErrorSettings: ...
    def __new__(cls: typing.Type[RuntimeBrokerErrorSettings]) -> RuntimeBrokerErrorSettings:...
    def get_error_options(self) -> ErrorOptions: ...
    def set_error_options(self, value: ErrorOptions) -> None: ...

class TracingStatusChangedEventArgs(_winrt.Object):
    enabled: _winrt.Boolean
    trace_level: CausalityTraceLevel
    @staticmethod
    def _from(obj: _winrt.Object) -> TracingStatusChangedEventArgs: ...

class IErrorReportingSettings(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> IErrorReportingSettings: ...
    def get_error_options(self) -> ErrorOptions: ...
    def set_error_options(self, value: ErrorOptions) -> None: ...

class IFileLoggingSession(_winrt.Object):
    name: str
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> IFileLoggingSession: ...
    @typing.overload
    def add_logging_channel(self, logging_channel: typing.Optional[ILoggingChannel]) -> None: ...
    @typing.overload
    def add_logging_channel(self, logging_channel: typing.Optional[ILoggingChannel], max_level: LoggingLevel) -> None: ...
    def close(self) -> None: ...
    def close_and_save_to_file_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFile]: ...
    def remove_logging_channel(self, logging_channel: typing.Optional[ILoggingChannel]) -> None: ...
    def add_log_file_generated(self, handler: winsdk.windows.foundation.TypedEventHandler[IFileLoggingSession, LogFileGeneratedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_log_file_generated(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class ILoggingChannel(_winrt.Object):
    enabled: _winrt.Boolean
    level: LoggingLevel
    name: str
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> ILoggingChannel: ...
    def close(self) -> None: ...
    @typing.overload
    def log_message(self, event_string: str) -> None: ...
    @typing.overload
    def log_message(self, event_string: str, level: LoggingLevel) -> None: ...
    @typing.overload
    def log_value_pair(self, value1: str, value2: _winrt.Int32) -> None: ...
    @typing.overload
    def log_value_pair(self, value1: str, value2: _winrt.Int32, level: LoggingLevel) -> None: ...
    def add_logging_enabled(self, handler: winsdk.windows.foundation.TypedEventHandler[ILoggingChannel, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_logging_enabled(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class ILoggingSession(_winrt.Object):
    name: str
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> ILoggingSession: ...
    @typing.overload
    def add_logging_channel(self, logging_channel: typing.Optional[ILoggingChannel]) -> None: ...
    @typing.overload
    def add_logging_channel(self, logging_channel: typing.Optional[ILoggingChannel], max_level: LoggingLevel) -> None: ...
    def close(self) -> None: ...
    def remove_logging_channel(self, logging_channel: typing.Optional[ILoggingChannel]) -> None: ...
    def save_to_file_async(self, folder: typing.Optional[winsdk.windows.storage.IStorageFolder], file_name: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFile]: ...

class ILoggingTarget(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> ILoggingTarget: ...
    @typing.overload
    def is_enabled(self) -> _winrt.Boolean: ...
    @typing.overload
    def is_enabled(self, level: LoggingLevel) -> _winrt.Boolean: ...
    @typing.overload
    def is_enabled(self, level: LoggingLevel, keywords: _winrt.Int64) -> _winrt.Boolean: ...
    @typing.overload
    def log_event(self, event_name: str) -> None: ...
    @typing.overload
    def log_event(self, event_name: str, fields: typing.Optional[LoggingFields]) -> None: ...
    @typing.overload
    def log_event(self, event_name: str, fields: typing.Optional[LoggingFields], level: LoggingLevel) -> None: ...
    @typing.overload
    def log_event(self, event_name: str, fields: typing.Optional[LoggingFields], level: LoggingLevel, options: typing.Optional[LoggingOptions]) -> None: ...
    @typing.overload
    def start_activity(self, start_event_name: str) -> typing.Optional[LoggingActivity]: ...
    @typing.overload
    def start_activity(self, start_event_name: str, fields: typing.Optional[LoggingFields]) -> typing.Optional[LoggingActivity]: ...
    @typing.overload
    def start_activity(self, start_event_name: str, fields: typing.Optional[LoggingFields], level: LoggingLevel) -> typing.Optional[LoggingActivity]: ...
    @typing.overload
    def start_activity(self, start_event_name: str, fields: typing.Optional[LoggingFields], level: LoggingLevel, options: typing.Optional[LoggingOptions]) -> typing.Optional[LoggingActivity]: ...


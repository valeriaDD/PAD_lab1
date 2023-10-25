# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bookings.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto import service_discovery_pb2 as proto_dot_service__discovery__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bookings.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x62ookings.proto\x1a\x17service_discovery.proto\"Z\n\x12\x42ookScooterRequest\x12\x12\n\nscooter_id\x18\x01 \x01(\t\x12\r\n\x05start\x18\x02 \x01(\t\x12\x12\n\nuser_email\x18\x03 \x01(\t\x12\r\n\x05title\x18\x04 \x01(\t\"t\n\x13\x42ookScooterResponse\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05start\x18\x02 \x01(\t\x12\x12\n\nuser_email\x18\x03 \x01(\t\x12\x12\n\nscooter_id\x18\x04 \x01(\t\x12\x0b\n\x03\x65nd\x18\x05 \x01(\t\x12\r\n\x05title\x18\x06 \x01(\t\"\x1c\n\x0e\x45ndRideRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"\x1f\n\x11GetBookingRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"@\n\x16GetAllBookingsResponse\x12&\n\x08\x62ookings\x18\x01 \x03(\x0b\x32\x14.BookScooterResponse2\xe8\x01\n\x0f\x42ookingsService\x12\x38\n\x0b\x42ookScooter\x12\x13.BookScooterRequest\x1a\x14.BookScooterResponse\x12\x30\n\x07\x45ndRide\x12\x0f.EndRideRequest\x1a\x14.BookScooterResponse\x12\x36\n\nGetBooking\x12\x12.GetBookingRequest\x1a\x14.BookScooterResponse\x12\x31\n\x0eGetAllBookings\x12\x06.Empty\x1a\x17.GetAllBookingsResponseb\x06proto3'
  ,
  dependencies=[proto_dot_service__discovery__pb2.DESCRIPTOR, ])




_BOOKSCOOTERREQUEST = _descriptor.Descriptor(
  name='BookScooterRequest',
  full_name='BookScooterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='scooter_id', full_name='BookScooterRequest.scooter_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start', full_name='BookScooterRequest.start', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_email', full_name='BookScooterRequest.user_email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='BookScooterRequest.title', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=133,
)


_BOOKSCOOTERRESPONSE = _descriptor.Descriptor(
  name='BookScooterResponse',
  full_name='BookScooterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='BookScooterResponse.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start', full_name='BookScooterResponse.start', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_email', full_name='BookScooterResponse.user_email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scooter_id', full_name='BookScooterResponse.scooter_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end', full_name='BookScooterResponse.end', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='BookScooterResponse.title', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=251,
)


_ENDRIDEREQUEST = _descriptor.Descriptor(
  name='EndRideRequest',
  full_name='EndRideRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='EndRideRequest.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=253,
  serialized_end=281,
)


_GETBOOKINGREQUEST = _descriptor.Descriptor(
  name='GetBookingRequest',
  full_name='GetBookingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='GetBookingRequest.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=283,
  serialized_end=314,
)


_GETALLBOOKINGSRESPONSE = _descriptor.Descriptor(
  name='GetAllBookingsResponse',
  full_name='GetAllBookingsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bookings', full_name='GetAllBookingsResponse.bookings', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=316,
  serialized_end=380,
)

_GETALLBOOKINGSRESPONSE.fields_by_name['bookings'].message_type = _BOOKSCOOTERRESPONSE
DESCRIPTOR.message_types_by_name['BookScooterRequest'] = _BOOKSCOOTERREQUEST
DESCRIPTOR.message_types_by_name['BookScooterResponse'] = _BOOKSCOOTERRESPONSE
DESCRIPTOR.message_types_by_name['EndRideRequest'] = _ENDRIDEREQUEST
DESCRIPTOR.message_types_by_name['GetBookingRequest'] = _GETBOOKINGREQUEST
DESCRIPTOR.message_types_by_name['GetAllBookingsResponse'] = _GETALLBOOKINGSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BookScooterRequest = _reflection.GeneratedProtocolMessageType('BookScooterRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOOKSCOOTERREQUEST,
  '__module__' : 'bookings_pb2'
  # @@protoc_insertion_point(class_scope:BookScooterRequest)
  })
_sym_db.RegisterMessage(BookScooterRequest)

BookScooterResponse = _reflection.GeneratedProtocolMessageType('BookScooterResponse', (_message.Message,), {
  'DESCRIPTOR' : _BOOKSCOOTERRESPONSE,
  '__module__' : 'bookings_pb2'
  # @@protoc_insertion_point(class_scope:BookScooterResponse)
  })
_sym_db.RegisterMessage(BookScooterResponse)

EndRideRequest = _reflection.GeneratedProtocolMessageType('EndRideRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENDRIDEREQUEST,
  '__module__' : 'bookings_pb2'
  # @@protoc_insertion_point(class_scope:EndRideRequest)
  })
_sym_db.RegisterMessage(EndRideRequest)

GetBookingRequest = _reflection.GeneratedProtocolMessageType('GetBookingRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBOOKINGREQUEST,
  '__module__' : 'bookings_pb2'
  # @@protoc_insertion_point(class_scope:GetBookingRequest)
  })
_sym_db.RegisterMessage(GetBookingRequest)

GetAllBookingsResponse = _reflection.GeneratedProtocolMessageType('GetAllBookingsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETALLBOOKINGSRESPONSE,
  '__module__' : 'bookings_pb2'
  # @@protoc_insertion_point(class_scope:GetAllBookingsResponse)
  })
_sym_db.RegisterMessage(GetAllBookingsResponse)



_BOOKINGSSERVICE = _descriptor.ServiceDescriptor(
  name='BookingsService',
  full_name='BookingsService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=383,
  serialized_end=615,
  methods=[
  _descriptor.MethodDescriptor(
    name='BookScooter',
    full_name='BookingsService.BookScooter',
    index=0,
    containing_service=None,
    input_type=_BOOKSCOOTERREQUEST,
    output_type=_BOOKSCOOTERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EndRide',
    full_name='BookingsService.EndRide',
    index=1,
    containing_service=None,
    input_type=_ENDRIDEREQUEST,
    output_type=_BOOKSCOOTERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBooking',
    full_name='BookingsService.GetBooking',
    index=2,
    containing_service=None,
    input_type=_GETBOOKINGREQUEST,
    output_type=_BOOKSCOOTERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllBookings',
    full_name='BookingsService.GetAllBookings',
    index=3,
    containing_service=None,
    input_type=proto_dot_service__discovery__pb2._EMPTY,
    output_type=_GETALLBOOKINGSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BOOKINGSSERVICE)

DESCRIPTOR.services_by_name['BookingsService'] = _BOOKINGSSERVICE

# @@protoc_insertion_point(module_scope)

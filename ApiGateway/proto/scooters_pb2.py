# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scooters.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto import service_discovery_pb2 as service__discovery__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='scooters.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0escooters.proto\x1a\x17service_discovery.proto\"\x1f\n\x11GetScooterRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"i\n\x14UpdateScooterRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05label\x18\x02 \x01(\t\x12\x0f\n\x07\x62\x61ttery\x18\x03 \x01(\x05\x12\x10\n\x08location\x18\x04 \x01(\t\x12\x13\n\x0bis_charging\x18\x05 \x01(\x08\"\"\n\x14\x44\x65leteScooterRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"]\n\x14\x43reateScooterRequest\x12\r\n\x05label\x18\x01 \x01(\t\x12\x0f\n\x07\x62\x61ttery\x18\x02 \x01(\x05\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x13\n\x0bis_charging\x18\x04 \x01(\x08\"z\n\x12GetScooterResponse\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05label\x18\x02 \x01(\t\x12\x0f\n\x07\x62\x61ttery\x18\x03 \x01(\x05\x12\x10\n\x08location\x18\x04 \x01(\t\x12\x13\n\x0bis_charging\x18\x05 \x01(\x08\x12\x11\n\tavailable\x18\x06 \x01(\x08\"7\n\x16SetAvailabilityRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x11\n\tavailable\x18\x02 \x01(\x08\"?\n\x16GetAllScootersResponse\x12%\n\x08scooters\x18\x01 \x03(\x0b\x32\x13.GetScooterResponse\"j\n\x15\x43reateScooterResponse\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05label\x18\x02 \x01(\t\x12\x0f\n\x07\x62\x61ttery\x18\x03 \x01(\x05\x12\x10\n\x08location\x18\x04 \x01(\t\x12\x13\n\x0bis_charging\x18\x05 \x01(\x08\x32\xd5\x02\n\x0eScooterService\x12\x35\n\nGetScooter\x12\x12.GetScooterRequest\x1a\x13.GetScooterResponse\x12\x31\n\x0eGetAllScooters\x12\x06.Empty\x1a\x17.GetAllScootersResponse\x12.\n\rUpdateScooter\x12\x15.UpdateScooterRequest\x1a\x06.Empty\x12.\n\rDeleteScooter\x12\x15.DeleteScooterRequest\x1a\x06.Empty\x12>\n\rCreateScooter\x12\x15.CreateScooterRequest\x1a\x16.CreateScooterResponse\x12\x39\n\x16SetScooterAvailability\x12\x17.SetAvailabilityRequest\x1a\x06.Emptyb\x06proto3'
  ,
  dependencies=[service__discovery__pb2.DESCRIPTOR,])




_GETSCOOTERREQUEST = _descriptor.Descriptor(
  name='GetScooterRequest',
  full_name='GetScooterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='GetScooterRequest.id', index=0,
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
  serialized_start=43,
  serialized_end=74,
)


_UPDATESCOOTERREQUEST = _descriptor.Descriptor(
  name='UpdateScooterRequest',
  full_name='UpdateScooterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='UpdateScooterRequest.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='UpdateScooterRequest.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='battery', full_name='UpdateScooterRequest.battery', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='UpdateScooterRequest.location', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_charging', full_name='UpdateScooterRequest.is_charging', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=76,
  serialized_end=181,
)


_DELETESCOOTERREQUEST = _descriptor.Descriptor(
  name='DeleteScooterRequest',
  full_name='DeleteScooterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='DeleteScooterRequest.id', index=0,
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
  serialized_start=183,
  serialized_end=217,
)


_CREATESCOOTERREQUEST = _descriptor.Descriptor(
  name='CreateScooterRequest',
  full_name='CreateScooterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='CreateScooterRequest.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='battery', full_name='CreateScooterRequest.battery', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='CreateScooterRequest.location', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_charging', full_name='CreateScooterRequest.is_charging', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=219,
  serialized_end=312,
)


_GETSCOOTERRESPONSE = _descriptor.Descriptor(
  name='GetScooterResponse',
  full_name='GetScooterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='GetScooterResponse.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='GetScooterResponse.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='battery', full_name='GetScooterResponse.battery', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='GetScooterResponse.location', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_charging', full_name='GetScooterResponse.is_charging', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='available', full_name='GetScooterResponse.available', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=314,
  serialized_end=436,
)


_SETAVAILABILITYREQUEST = _descriptor.Descriptor(
  name='SetAvailabilityRequest',
  full_name='SetAvailabilityRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SetAvailabilityRequest.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='available', full_name='SetAvailabilityRequest.available', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=438,
  serialized_end=493,
)


_GETALLSCOOTERSRESPONSE = _descriptor.Descriptor(
  name='GetAllScootersResponse',
  full_name='GetAllScootersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='scooters', full_name='GetAllScootersResponse.scooters', index=0,
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
  serialized_start=495,
  serialized_end=558,
)


_CREATESCOOTERRESPONSE = _descriptor.Descriptor(
  name='CreateScooterResponse',
  full_name='CreateScooterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='CreateScooterResponse.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='CreateScooterResponse.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='battery', full_name='CreateScooterResponse.battery', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='CreateScooterResponse.location', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_charging', full_name='CreateScooterResponse.is_charging', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=560,
  serialized_end=666,
)

_GETALLSCOOTERSRESPONSE.fields_by_name['scooters'].message_type = _GETSCOOTERRESPONSE
DESCRIPTOR.message_types_by_name['GetScooterRequest'] = _GETSCOOTERREQUEST
DESCRIPTOR.message_types_by_name['UpdateScooterRequest'] = _UPDATESCOOTERREQUEST
DESCRIPTOR.message_types_by_name['DeleteScooterRequest'] = _DELETESCOOTERREQUEST
DESCRIPTOR.message_types_by_name['CreateScooterRequest'] = _CREATESCOOTERREQUEST
DESCRIPTOR.message_types_by_name['GetScooterResponse'] = _GETSCOOTERRESPONSE
DESCRIPTOR.message_types_by_name['SetAvailabilityRequest'] = _SETAVAILABILITYREQUEST
DESCRIPTOR.message_types_by_name['GetAllScootersResponse'] = _GETALLSCOOTERSRESPONSE
DESCRIPTOR.message_types_by_name['CreateScooterResponse'] = _CREATESCOOTERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetScooterRequest = _reflection.GeneratedProtocolMessageType('GetScooterRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSCOOTERREQUEST,
  '__module__' : 'scooters_pb2'
  # @@protoc_insertion_point(class_scope:GetScooterRequest)
  })
_sym_db.RegisterMessage(GetScooterRequest)

UpdateScooterRequest = _reflection.GeneratedProtocolMessageType('UpdateScooterRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESCOOTERREQUEST,
  '__module__' : 'scooters_pb2'
  # @@protoc_insertion_point(class_scope:UpdateScooterRequest)
  })
_sym_db.RegisterMessage(UpdateScooterRequest)

DeleteScooterRequest = _reflection.GeneratedProtocolMessageType('DeleteScooterRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETESCOOTERREQUEST,
  '__module__' : 'scooters_pb2'
  # @@protoc_insertion_point(class_scope:DeleteScooterRequest)
  })
_sym_db.RegisterMessage(DeleteScooterRequest)

CreateScooterRequest = _reflection.GeneratedProtocolMessageType('CreateScooterRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESCOOTERREQUEST,
  '__module__' : 'scooters_pb2'
  # @@protoc_insertion_point(class_scope:CreateScooterRequest)
  })
_sym_db.RegisterMessage(CreateScooterRequest)

GetScooterResponse = _reflection.GeneratedProtocolMessageType('GetScooterResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSCOOTERRESPONSE,
  '__module__' : 'scooters_pb2'
  # @@protoc_insertion_point(class_scope:GetScooterResponse)
  })
_sym_db.RegisterMessage(GetScooterResponse)

SetAvailabilityRequest = _reflection.GeneratedProtocolMessageType('SetAvailabilityRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETAVAILABILITYREQUEST,
  '__module__' : 'scooters_pb2'
  # @@protoc_insertion_point(class_scope:SetAvailabilityRequest)
  })
_sym_db.RegisterMessage(SetAvailabilityRequest)

GetAllScootersResponse = _reflection.GeneratedProtocolMessageType('GetAllScootersResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETALLSCOOTERSRESPONSE,
  '__module__' : 'scooters_pb2'
  # @@protoc_insertion_point(class_scope:GetAllScootersResponse)
  })
_sym_db.RegisterMessage(GetAllScootersResponse)

CreateScooterResponse = _reflection.GeneratedProtocolMessageType('CreateScooterResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATESCOOTERRESPONSE,
  '__module__' : 'scooters_pb2'
  # @@protoc_insertion_point(class_scope:CreateScooterResponse)
  })
_sym_db.RegisterMessage(CreateScooterResponse)



_SCOOTERSERVICE = _descriptor.ServiceDescriptor(
  name='ScooterService',
  full_name='ScooterService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=669,
  serialized_end=1010,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetScooter',
    full_name='ScooterService.GetScooter',
    index=0,
    containing_service=None,
    input_type=_GETSCOOTERREQUEST,
    output_type=_GETSCOOTERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllScooters',
    full_name='ScooterService.GetAllScooters',
    index=1,
    containing_service=None,
    input_type=service__discovery__pb2._EMPTY,
    output_type=_GETALLSCOOTERSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateScooter',
    full_name='ScooterService.UpdateScooter',
    index=2,
    containing_service=None,
    input_type=_UPDATESCOOTERREQUEST,
    output_type=service__discovery__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteScooter',
    full_name='ScooterService.DeleteScooter',
    index=3,
    containing_service=None,
    input_type=_DELETESCOOTERREQUEST,
    output_type=service__discovery__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateScooter',
    full_name='ScooterService.CreateScooter',
    index=4,
    containing_service=None,
    input_type=_CREATESCOOTERREQUEST,
    output_type=_CREATESCOOTERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetScooterAvailability',
    full_name='ScooterService.SetScooterAvailability',
    index=5,
    containing_service=None,
    input_type=_SETAVAILABILITYREQUEST,
    output_type=service__discovery__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SCOOTERSERVICE)

DESCRIPTOR.services_by_name['ScooterService'] = _SCOOTERSERVICE

# @@protoc_insertion_point(module_scope)

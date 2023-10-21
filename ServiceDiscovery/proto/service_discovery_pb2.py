# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/service_discovery.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/service_discovery.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1dproto/service_discovery.proto\"?\n\x0bServiceInfo\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\t\"&\n\x0eServiceRequest\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\"\x07\n\x05\x45mpty\"\x1e\n\x0cHealthStatus\x12\x0e\n\x06status\x18\x01 \x01(\x08\x32\x92\x01\n\x0fServiceRegistry\x12\'\n\x0fRegisterService\x12\x0c.ServiceInfo\x1a\x06.Empty\x12\x30\n\x0f\x44iscoverService\x12\x0f.ServiceRequest\x1a\x0c.ServiceInfo\x12$\n\x0b\x43heckHealth\x12\x06.Empty\x1a\r.HealthStatusb\x06proto3'
)




_SERVICEINFO = _descriptor.Descriptor(
  name='ServiceInfo',
  full_name='ServiceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_name', full_name='ServiceInfo.service_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host', full_name='ServiceInfo.host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='ServiceInfo.port', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=33,
  serialized_end=96,
)


_SERVICEREQUEST = _descriptor.Descriptor(
  name='ServiceRequest',
  full_name='ServiceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_name', full_name='ServiceRequest.service_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=98,
  serialized_end=136,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=138,
  serialized_end=145,
)


_HEALTHSTATUS = _descriptor.Descriptor(
  name='HealthStatus',
  full_name='HealthStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='HealthStatus.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=147,
  serialized_end=177,
)

DESCRIPTOR.message_types_by_name['ServiceInfo'] = _SERVICEINFO
DESCRIPTOR.message_types_by_name['ServiceRequest'] = _SERVICEREQUEST
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['HealthStatus'] = _HEALTHSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServiceInfo = _reflection.GeneratedProtocolMessageType('ServiceInfo', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEINFO,
  '__module__' : 'proto.service_discovery_pb2'
  # @@protoc_insertion_point(class_scope:ServiceInfo)
  })
_sym_db.RegisterMessage(ServiceInfo)

ServiceRequest = _reflection.GeneratedProtocolMessageType('ServiceRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEREQUEST,
  '__module__' : 'proto.service_discovery_pb2'
  # @@protoc_insertion_point(class_scope:ServiceRequest)
  })
_sym_db.RegisterMessage(ServiceRequest)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'proto.service_discovery_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

HealthStatus = _reflection.GeneratedProtocolMessageType('HealthStatus', (_message.Message,), {
  'DESCRIPTOR' : _HEALTHSTATUS,
  '__module__' : 'proto.service_discovery_pb2'
  # @@protoc_insertion_point(class_scope:HealthStatus)
  })
_sym_db.RegisterMessage(HealthStatus)



_SERVICEREGISTRY = _descriptor.ServiceDescriptor(
  name='ServiceRegistry',
  full_name='ServiceRegistry',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=180,
  serialized_end=326,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterService',
    full_name='ServiceRegistry.RegisterService',
    index=0,
    containing_service=None,
    input_type=_SERVICEINFO,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DiscoverService',
    full_name='ServiceRegistry.DiscoverService',
    index=1,
    containing_service=None,
    input_type=_SERVICEREQUEST,
    output_type=_SERVICEINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CheckHealth',
    full_name='ServiceRegistry.CheckHealth',
    index=2,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_HEALTHSTATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVICEREGISTRY)

DESCRIPTOR.services_by_name['ServiceRegistry'] = _SERVICEREGISTRY

# @@protoc_insertion_point(module_scope)

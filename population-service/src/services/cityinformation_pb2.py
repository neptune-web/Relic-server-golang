# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cityinformation.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cityinformation.proto',
  package='cityinformation',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x15\x63ityinformation.proto\x12\x0f\x63ityinformation\"H\n\rSearchRequest\x12\x0c\n\x04\x63ity\x18\x01 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x02 \x01(\t\x12\x0b\n\x03lat\x18\x03 \x01(\t\x12\x0b\n\x03lon\x18\x04 \x01(\t\":\n\x0eSearchResponse\x12\x14\n\x0cnearbyCities\x18\x01 \x01(\t\x12\x12\n\npopulation\x18\x02 \x01(\t2f\n\x0b\x43ityService\x12W\n\x12GetCityInformation\x12\x1e.cityinformation.SearchRequest\x1a\x1f.cityinformation.SearchResponse\"\x00\x62\x06proto3'
)




_SEARCHREQUEST = _descriptor.Descriptor(
  name='SearchRequest',
  full_name='cityinformation.SearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='city', full_name='cityinformation.SearchRequest.city', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='country', full_name='cityinformation.SearchRequest.country', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lat', full_name='cityinformation.SearchRequest.lat', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lon', full_name='cityinformation.SearchRequest.lon', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=42,
  serialized_end=114,
)


_SEARCHRESPONSE = _descriptor.Descriptor(
  name='SearchResponse',
  full_name='cityinformation.SearchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nearbyCities', full_name='cityinformation.SearchResponse.nearbyCities', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='population', full_name='cityinformation.SearchResponse.population', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=116,
  serialized_end=174,
)

DESCRIPTOR.message_types_by_name['SearchRequest'] = _SEARCHREQUEST
DESCRIPTOR.message_types_by_name['SearchResponse'] = _SEARCHRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchRequest = _reflection.GeneratedProtocolMessageType('SearchRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREQUEST,
  '__module__' : 'cityinformation_pb2'
  # @@protoc_insertion_point(class_scope:cityinformation.SearchRequest)
  })
_sym_db.RegisterMessage(SearchRequest)

SearchResponse = _reflection.GeneratedProtocolMessageType('SearchResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHRESPONSE,
  '__module__' : 'cityinformation_pb2'
  # @@protoc_insertion_point(class_scope:cityinformation.SearchResponse)
  })
_sym_db.RegisterMessage(SearchResponse)



_CITYSERVICE = _descriptor.ServiceDescriptor(
  name='CityService',
  full_name='cityinformation.CityService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=176,
  serialized_end=278,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCityInformation',
    full_name='cityinformation.CityService.GetCityInformation',
    index=0,
    containing_service=None,
    input_type=_SEARCHREQUEST,
    output_type=_SEARCHRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CITYSERVICE)

DESCRIPTOR.services_by_name['CityService'] = _CITYSERVICE

# @@protoc_insertion_point(module_scope)
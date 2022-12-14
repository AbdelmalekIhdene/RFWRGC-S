# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0btypes.proto\"\xdf\x01\n\x03RFW\x12\n\n\x02Id\x18\x01 \x01(\x05\x12%\n\rbenchmarkType\x18\x02 \x01(\x0e\x32\x0e.BenchmarkType\x12\'\n\x0eworkloadMetric\x18\x03 \x01(\x0e\x32\x0f.WorkloadMetric\x12\x13\n\x0bsampleCount\x18\x04 \x01(\x05\x12\x0f\n\x07\x62\x61tchId\x18\x05 \x01(\x05\x12\x12\n\nbatchCount\x18\x06 \x01(\x05\x12\x1b\n\x08\x64\x61taType\x18\x07 \x01(\x0e\x32\t.DataType\x12%\n\ranalyticsType\x18\x08 \x01(\x0e\x32\x0e.AnalyticsType\"S\n\x03RFD\x12\n\n\x02Id\x18\x01 \x01(\x05\x12\x13\n\x0blastBatchId\x18\x02 \x01(\x05\x12\x13\n\x07samples\x18\x03 \x03(\x01\x42\x02\x10\x01\x12\x16\n\x0e\x61nalyticsValue\x18\x04 \x01(\x01**\n\rBenchmarkType\x12\x0c\n\x08\x44VDSTORE\x10\x00\x12\x0b\n\x07NDBENCH\x10\x01*F\n\x0eWorkloadMetric\x12\x07\n\x03\x43PU\x10\x00\x12\x0e\n\nNETWORK_IN\x10\x01\x12\x0f\n\x0bNETWORK_OUT\x10\x02\x12\n\n\x06MEMORY\x10\x03*%\n\x08\x44\x61taType\x12\x0c\n\x08TRAINING\x10\x00\x12\x0b\n\x07TESTING\x10\x01*[\n\rAnalyticsType\x12\x08\n\x04T10P\x10\x00\x12\x08\n\x04T50P\x10\x01\x12\x08\n\x04T95P\x10\x02\x12\x08\n\x04T99P\x10\x03\x12\x07\n\x03\x41VG\x10\x04\x12\x07\n\x03STD\x10\x05\x12\x07\n\x03MAX\x10\x06\x12\x07\n\x03MIN\x10\x07\x62\x06proto3')

_BENCHMARKTYPE = DESCRIPTOR.enum_types_by_name['BenchmarkType']
BenchmarkType = enum_type_wrapper.EnumTypeWrapper(_BENCHMARKTYPE)
_WORKLOADMETRIC = DESCRIPTOR.enum_types_by_name['WorkloadMetric']
WorkloadMetric = enum_type_wrapper.EnumTypeWrapper(_WORKLOADMETRIC)
_DATATYPE = DESCRIPTOR.enum_types_by_name['DataType']
DataType = enum_type_wrapper.EnumTypeWrapper(_DATATYPE)
_ANALYTICSTYPE = DESCRIPTOR.enum_types_by_name['AnalyticsType']
AnalyticsType = enum_type_wrapper.EnumTypeWrapper(_ANALYTICSTYPE)
DVDSTORE = 0
NDBENCH = 1
CPU = 0
NETWORK_IN = 1
NETWORK_OUT = 2
MEMORY = 3
TRAINING = 0
TESTING = 1
T10P = 0
T50P = 1
T95P = 2
T99P = 3
AVG = 4
STD = 5
MAX = 6
MIN = 7


_RFW = DESCRIPTOR.message_types_by_name['RFW']
_RFD = DESCRIPTOR.message_types_by_name['RFD']
RFW = _reflection.GeneratedProtocolMessageType('RFW', (_message.Message,), {
  'DESCRIPTOR' : _RFW,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:RFW)
  })
_sym_db.RegisterMessage(RFW)

RFD = _reflection.GeneratedProtocolMessageType('RFD', (_message.Message,), {
  'DESCRIPTOR' : _RFD,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:RFD)
  })
_sym_db.RegisterMessage(RFD)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RFD.fields_by_name['samples']._options = None
  _RFD.fields_by_name['samples']._serialized_options = b'\020\001'
  _BENCHMARKTYPE._serialized_start=326
  _BENCHMARKTYPE._serialized_end=368
  _WORKLOADMETRIC._serialized_start=370
  _WORKLOADMETRIC._serialized_end=440
  _DATATYPE._serialized_start=442
  _DATATYPE._serialized_end=479
  _ANALYTICSTYPE._serialized_start=481
  _ANALYTICSTYPE._serialized_end=572
  _RFW._serialized_start=16
  _RFW._serialized_end=239
  _RFD._serialized_start=241
  _RFD._serialized_end=324
# @@protoc_insertion_point(module_scope)

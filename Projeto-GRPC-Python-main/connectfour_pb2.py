# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: connectfour.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x63onnectfour.proto\x12\x0b\x63onnectfour\"\x1a\n\nPlayerInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\"8\n\x10\x43onnectionStatus\x12\x11\n\tconnected\x18\x01 \x01(\x08\x12\x11\n\tplayer_id\x18\x02 \x01(\x05\"&\n\x04Move\x12\x11\n\tplayer_id\x18\x01 \x01(\x05\x12\x0b\n\x03\x63ol\x18\x02 \x01(\x05\"T\n\nGameStatus\x12\x12\n\nvalid_move\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x11\n\tgame_over\x18\x03 \x01(\x08\x12\x0e\n\x06winner\x18\x04 \x01(\x05\"c\n\nGameUpdate\x12!\n\x05\x62oard\x18\x01 \x01(\x0b\x32\x12.connectfour.Board\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x11\n\tgame_over\x18\x03 \x01(\x08\x12\x0e\n\x06winner\x18\x04 \x01(\x05\"\'\n\x05\x42oard\x12\x1e\n\x04rows\x18\x01 \x03(\x0b\x32\x10.connectfour.Row\"\x14\n\x03Row\x12\r\n\x05\x63\x65lls\x18\x01 \x03(\t2\xca\x01\n\x0b\x43onnectFour\x12\x41\n\x07\x43onnect\x12\x17.connectfour.PlayerInfo\x1a\x1d.connectfour.ConnectionStatus\x12\x36\n\x08MakeMove\x12\x11.connectfour.Move\x1a\x17.connectfour.GameStatus\x12@\n\nGetUpdates\x12\x17.connectfour.PlayerInfo\x1a\x17.connectfour.GameUpdate0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'connectfour_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PLAYERINFO']._serialized_start=34
  _globals['_PLAYERINFO']._serialized_end=60
  _globals['_CONNECTIONSTATUS']._serialized_start=62
  _globals['_CONNECTIONSTATUS']._serialized_end=118
  _globals['_MOVE']._serialized_start=120
  _globals['_MOVE']._serialized_end=158
  _globals['_GAMESTATUS']._serialized_start=160
  _globals['_GAMESTATUS']._serialized_end=244
  _globals['_GAMEUPDATE']._serialized_start=246
  _globals['_GAMEUPDATE']._serialized_end=345
  _globals['_BOARD']._serialized_start=347
  _globals['_BOARD']._serialized_end=386
  _globals['_ROW']._serialized_start=388
  _globals['_ROW']._serialized_end=408
  _globals['_CONNECTFOUR']._serialized_start=411
  _globals['_CONNECTFOUR']._serialized_end=613
# @@protoc_insertion_point(module_scope)
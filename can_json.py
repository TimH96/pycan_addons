"""
can_json.py
"""

import json
from can import Message

MESSAGE_ATTRIBUTES = {
    "arbitration_id",
    "bitrate_switch",
    "channel",
    "data",
    "dlc",
    "error_state_indicator",
    "is_error_frame",
    "is_extended_id",
    "is_fd",
    "is_remote_frame",
    "timestamp"
}


def json_parse(self: Message, json_string: str) -> None:
    """Decodes a json-encoded can.Message and passes its attribute values to object instance"""
    # parse json
    this_dict: dict = json.loads(json_string)
    # iterate over all dict items
    for item in this_dict.items():
        # special case 'data', requires typecast
        if item[0] == "data":
            this_data = bytearray()
            for ele in item[1]:
                this_data.append(ele)
            setattr(self, 'data', this_data)
        # normal case
        elif item[0] in MESSAGE_ATTRIBUTES:
            setattr(self, item[0], item[1])
        # json attribute not part of can.Message
        else:
            pass


def json_stringify(self: Message) -> str:
    """Encodes can.Message as json string and returns it"""
    # init and populate dict
    out : dict = {}
    for attr in MESSAGE_ATTRIBUTES:
        # special case data
        if attr == 'data':
            out['data'] = []
        # normal case
        else:
            out[attr] = self.__getattribute__(attr)
    # return exported json
    return json.dumps(out)

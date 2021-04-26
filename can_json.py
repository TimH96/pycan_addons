"""
can_json.py
"""

import json
from can import Message


def json_parse(self: Message, json_string: str) -> None:
    """Decodes a json-encoded can.Message and passes its attribute values to object instance"""
    # parse json
    this_dict: dict = json.loads(json_string)
    # iterate over all dict items
    for item in this_dict.items():
        # normal case
        if item[0] != "data":
            setattr(self, item[0], item[1])
        # special case 'data', requires typecast
        else:
            this_data = bytearray()
            for ele in item[1]:
                this_data.append(ele)
            setattr(self, 'data', this_data)


def json_stringify(self: Message) -> str:
    """Encodes can.Message as json string and returns it"""
    # init and populate dict
    this_dict = {}
    this_dict["arbitration_id"] = self.arbitration_id
    this_dict["bitrate_switch"] = self.bitrate_switch
    this_dict["channel"] = self.channel
    this_dict["dlc"] = self.dlc
    this_dict["error_state_indicator"] = self.error_state_indicator
    this_dict["is_error_frame"] = self.is_error_frame
    this_dict["is_extended_id"] = self.is_extended_id
    this_dict["is_fd"] = self.is_fd
    this_dict["is_remote_frame"] = self.is_remote_frame
    this_dict["timestamp"] = self.timestamp
    this_dict["data"] = []
    for ele in self.data:
        this_dict["data"].append(ele)
    # return exported json
    return json.dumps(this_dict)

"""
pycan_addons.can_json

Defines json import and export methods for can.Message class and attaches
them to said class

Supports the following attributes of can.Message:
    - arbitration_id
    - bitrate_switch
    - channel
    - data
    - dlc
    - error_state_indicator
    - is_error_frame
    - is_fd
    - is_remote_frame
    - timestamp
"""

import can
import json

def json_parse(
    self: can.Message, 
    json_string: str,
    on_parse_error: 'callback'=None,
    on_attribute_error: 'callback'=None
):
    """Decodes a json-encoded can.Message and passes its attribute values to object instance"""
    # parse json
    try:
        this_dict: dict = json.loads(json_string)
    except Exception as error:
        if on_parse_error:
            on_parse_error(error)
        return
    # iterate over all dict items
    for item in this_dict.items():
        try:
            # normal case
            if item[0] != "data":
                setattr(self, item[0], item[1])
            # special case 'data', requires typecast
            else:
                this_data = bytearray()
                for ele in item[1]:
                    this_data.append(ele)
                setattr(self, 'data', this_data)
        except Exception as error:
            if on_attribute_error:
                on_attribute_error(error)
            return 

def json_stringify(self: can.Message):
    """Encodes can.Message as json string and returns it"""
    # init and populate dict
    this_dict = {}
    this_dict["arbitration_id"] = self.arbitration_id
    this_dict["bitrate_switch"] = self.bitrate_switch
    this_dict["channel"] = self.channel
    this_dict["dlc"] = self.dlc
    this_dict["error_state_indicator"] = self.error_state_indicator
    this_dict["is_error_frame"] = self.is_error_frame
    this_dict["is_fd"] = self.is_fd
    this_dict["is_remote_frame"] = self.is_remote_frame
    this_dict["timestamp"] = self.timestamp
    this_dict["data"] = []
    for ele in self.data:
        this_dict["data"].append(ele)
    # return exported json
    return json.dumps(this_dict)

# add methods to can.Message class
setattr(can.Message, 'json_parse', json_parse)
setattr(can.Message, 'json_stringify', json_stringify)
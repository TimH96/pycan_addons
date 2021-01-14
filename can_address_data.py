"""
pycan_addons.can_address_data

Adds method to calculate CAN ID and object type of message based on 
CANopen standard to can.Message class
"""

import can

def get_address_data(self: can.Message):
    """Returns node ID and object type of message"""
    address_data = {}
    # get node ID
    address_data["node_id"] = self.arbitration_id & 0b000001111111
    # get object type, map taken from https://en.wikipedia.org/wiki/CANopen#Predefined_Connection_Set[7]
    object_map = {
        0x000                           : "NMT_CONTROL",
        0x001                           : "FAILSAFE",
        0x080                           : "SYNC",
        0x080 + address_data["node_id"] : "EMERGENCY",
        0x100                           : "TIMESTAMP",
        0x180 + address_data["node_id"] : "TPDO1",
        0x200 + address_data["node_id"] : "RPDO1",
        0x280 + address_data["node_id"] : "TPDO2",
        0x300 + address_data["node_id"] : "RPDO2",
        0x380 + address_data["node_id"] : "TPDO3",
        0x400 + address_data["node_id"] : "RPDO3",
        0x480 + address_data["node_id"] : "TPDO4",
        0x500 + address_data["node_id"] : "RPDO4",
        0x580 + address_data["node_id"] : "TSDO",
        0x600 + address_data["node_id"] : "RSDO",
        0x700 + address_data["node_id"] : "NMT_MONITORING",
        0x7E4 + address_data["node_id"] : "TLSS",
        0x7E5 + address_data["node_id"] : "RLSS",
    }
    address_data["object_type"] = object_map.get(self.arbitration_id, None)
    # retroactively overwrite node id for broadcasted objects
    if address_data["object_type"] in ["NMT_CONTROL", "FAILSAFE", "SYNC", "TIMESTAMP"]:
        address_data["node_id"] = -1
    # return final object
    return address_data

# add method to can.Message class
setattr(can.Message, 'get_address_data', get_address_data)
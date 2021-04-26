"""
can_address_data.py
"""

from can import Message


def get_object_map(id_offset: int) -> dict:
    """
    Returns ID to communication object mapping of a given CAN node ID.
    Map taken from https://en.wikipedia.org/wiki/CANopen#Predefined_Connection_Set[7]
    """
    return {
        0x000               : "NMT_CONTROL",
        0x001               : "FAILSAFE",
        0x080               : "SYNC",
        0x080 + id_offset   : "EMERGENCY",
        0x100               : "TIMESTAMP",
        0x180 + id_offset   : "TPDO1",
        0x200 + id_offset   : "RPDO1",
        0x280 + id_offset   : "TPDO2",
        0x300 + id_offset   : "RPDO2",
        0x380 + id_offset   : "TPDO3",
        0x400 + id_offset   : "RPDO3",
        0x480 + id_offset   : "TPDO4",
        0x500 + id_offset   : "RPDO4",
        0x580 + id_offset   : "TSDO",
        0x600 + id_offset   : "RSDO",
        0x700 + id_offset   : "NMT_MONITORING",
        0x7E4               : "TLSS",
        0x7E5               : "RLSS"
    }


def get_address_data(self: Message) -> dict:
    """Returns node ID and object type of a given message"""
    address_data : dict = {}
    # get node ID
    address_data["node_id"] = (self.arbitration_id & 0b000001111111)
    # get object type
    address_data["object_type"] = get_object_map(address_data['node_id']).get(self.arbitration_id, None)
    # retroactively overwrite node id for broadcasted objects
    if address_data["object_type"] in ["NMT_CONTROL", "FAILSAFE", "SYNC", "TIMESTAMP", "TLSS", "RLSS"]:
        address_data["node_id"] = -1
    # return final object
    return address_data

"""
class_bind.py
"""

from can                            import Message
from pycan_addons.can_json          import *
from pycan_addons.can_address_data  import *

# add methods to can.Message class
setattr(Message,    'get_address_data',    get_address_data)
setattr(Message,    'json_parse',          json_parse)
setattr(Message,    'json_stringify',      json_stringify)

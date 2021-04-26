# PyCAN addons

Adds the following utility methods to ``can.Message`` class of python-can module:
+ ``json_stringify`` - encodes message as json
+ ``json_parse`` - parses json format to object instance, counterpart to ``json_stringify``
+ ``get_address_data`` - extracts ID and object type from arbitration ID

### Usage
You can either import and call the functions with a given message as parameter:

```python
from can import Message
from pycan_addons.can_json import json_stringify, json_parse

msg = Message()
print(json_stringify(msg))
```
```python
>> {"arbitration_id": 0, "bitrate_switch": false, "channel": null, "dlc": 0, "error_state_indicator": false, "is_error_frame": false, "is_extended_id": true, "is_fd": false, "is_remote_frame": false, "timestamp": 0.0, "data": []}
``` 

Alternatively, via importing the ``class_bind`` module, you can bind them as methods to the ``can.Message`` class and directly call them on objects of that class:

```python
from can import Message
from pycan_addons import class_bind

msg = Message(arbitration_id=0x200 + 31)
print(msg.get_address_data())
```
```python
>> {'node_id': 31, 'object_type': 'RPDO1'}
``` 
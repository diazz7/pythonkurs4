from ncclient import manager
from rich import print
from xml.dom.minidom import parseString
import logging
from rich.logging import RichHandler


"""
logging.basicConfig(
    format="%(name)s - %(message)s",
    datefmt="[%X]",
    handlers=[RichHandler()],
)

logging.getLogger("ncclient.transport.ssh").setLevel(logging.DEBUG)
"""

filter = """
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname/>
    <version/>
    <interface/>
</native>
"""


def pretty_xml(config):
    return parseString(repr(config)).toprettyxml()


with manager.connect(
    host='10.18.10.21',
    port=830,
    username='ins',
    password='ins@lab',
    device_params={'name': 'csr'},
    hostkey_verify=False,
) as m:
    #   for c in m.server_capabilities:
    #       print(c)

    config = m.get_config(source="running", filter=("subtree", filter))
    print(config.data[0][1].text)

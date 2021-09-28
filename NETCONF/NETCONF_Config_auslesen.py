from ncclient import manager
from rich import print
from xml.dom.minidom import parseString


def pretty_xml(config):
    return parseString(repr(config)).toprettyxml()

with manager.connect(
    host="10.18.10.72",
    port=830,
    username="ins",
    password="ins@lab",
    device_params={"name": "csr"},
    hostkey_verify=False,
) as m:
    for c in m.server_capabilities:
        filter = """
        <native> xmlns="http://openconfig.net/yang/interfaces"/>
            <hostname/>
            <version/>
            <interface/>
        </native>
        """
        config = m.get_config(source="running", filter=("subtree", filter))
        print(pretty_xml(config))




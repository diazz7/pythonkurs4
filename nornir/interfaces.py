from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get

nr = InitNornir(config_file="nr-config.yaml")
result = nr.run(task=napalm_get, getters="interfaces")


hosts = nr.inventory.hosts.keys()
for host in hosts:
    print(f"Interfaces {host}:")
    for interface_name, values in result[host][0].result["interfaces"].items():
        print(f"Interface: {interface_name}, MAC-Address: {values['mac_address']}")


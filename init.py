from nornir import InitNornir
from nornir.core.task import Result
from nornir_utils.plugins.functions import print_result


def hello_world(task):
    return Result(host=task.host, result=f"{task.host.name} existiert!")


nr = InitNornir(config_file="nr-config.yaml")
result = nr.run(task=hello_world)
print_result(result)

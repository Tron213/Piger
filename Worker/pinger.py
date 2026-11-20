from icmplib import traceroute, ping, multiping



hosts = multiping(
    addresses,
    count=2,
    interval=0.5,
    timeout=2,
    concurrent_tasks=50,
    source=None,
    family=None,
    privileged=True,

)

for host in hosts:
    print(host.is_alive, host.address)
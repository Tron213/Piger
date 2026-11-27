from icmplib import traceroute, ping, multiping, async_multiping
import asyncio

async def multipings(addresses):
    hosts = await async_multiping(
        addresses,
        count=2,
        interval=0.5,
        timeout=2,
        concurrent_tasks=50,
        source=None,
        family=None,
        privileged=True,

    )
    result = []
    for host in hosts:
        
        result.append([host.is_alive, host.address, host.avg_rtt if host.is_alive else None])
        print(result)
    return result
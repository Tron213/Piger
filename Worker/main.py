from database import get_active_monitors

from pinger import multipings
import asyncio


async def main():
    while True:
        uuid_hosts = get_active_monitors()
        hosts = []
        for host in uuid_hosts:
            hosts.append(host[1])
        result = await multipings(hosts)
        print(result, uuid_hosts)
        await asyncio.sleep(60)
        
asyncio.run(main())
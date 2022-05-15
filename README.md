# betsapi_async
Python async SDK for betsapi.com

Full docs --> https://betsapi.com/docs/


**EXAMPLE:**
```
import asyncio
import aiohttp
from betsapi import BetsAPI,  BetsAPISamples


async def main():
    async with aiohttp.ClientSession() as session:
        api = BetsAPI('you_token', session)
        sample = BetsAPISamples(session)

        for sport_id, sport_name in api.r_sport_id.items():
            if sport_name not in ('Greyhounds', 'Snooker', 'Australian Rules', 'Futsal'):
                events = await api.in_play_events(sport_id)

        # If you don't have a token but want to play with the samples
        inplay_test = await sample.in_play_events
        print(inplay_test)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
```


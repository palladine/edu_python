# I
import asyncio

async def func1(n):
    for x in range(1, n+1):
        print('calls - {}, function - {}'.format(x, func1.__name__))
        await asyncio.sleep(3)


async def func2(n):
    for x in range(1, n+1):
        print('calls - {}, function - {}'.format(x, func2.__name__))
        await asyncio.sleep(2)


evloop = asyncio.get_event_loop()
tasks = [evloop.create_task(func1(6)), evloop.create_task(func2(6))]
wait_tasks = asyncio.wait(tasks)
evloop.run_until_complete(wait_tasks)
evloop.close()



# II
import aiohttp

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

async def call_url(url):
    print('Starting {}'.format(url))
    response = await aiohttp.get(url)
    data = await response.text()
    print('{}: {} bytes: {}'.format(url, len(data), data))
    return data

futures = [call_url(url) for url in urls]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))

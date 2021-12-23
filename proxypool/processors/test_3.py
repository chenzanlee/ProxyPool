import aiohttp
import asyncio
import threading
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) # 加上这一行
proxy='http://114.229.127.131:40154'

async def quest(url,  headers):
    con = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=con, trust_env=True) as sess: # 加上trust_env=True
        async with sess.get(url=url, headers=headers, proxy=proxy) as res:
            return await res.read()


def forever(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


# http://www.zdopen.com/PrivateProxy/GetIP/?api=202112231751318012&akey=e557eaeee9293d85&count=1&type=1
if __name__ == '__main__':
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}
    url = 'https://baidu.com'

    loop = asyncio.new_event_loop()
    t = threading.Thread(target=forever, args=(loop,))
    t.setDaemon(True)
    t.start()
    ret = asyncio.run_coroutine_threadsafe(quest(url, headers), loop)
    print(ret.result())
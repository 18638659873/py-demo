# 使用协程 爬取一本小说
# pip install aiofiles
import json

import aiohttp
import asyncio
import requests
import aiofiles


# 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4356290733"}'
# 'http://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4356290733","cid":"4356290733|1569830905","need_bookinfo":1}'


async def getCatalog(url):
    resp = requests.get(url)
    dic = resp.json()
    tasks = []
    for item in dic['data']['novel']['items']:
        title = item['title']
        cid = item['cid']
        tasks.append(asyncio.create_task(aiodownload(cid, b_id, title)))
    await asyncio.wait(tasks)


async def aiodownload(cid, b_id, title):
    data = {
        "book_id": b_id,
        "cid": f"{b_id}|{cid}",
        "need_bookinfo": 1
    }
    data = json.dumps(data)
    url = f'http://dushu.baidu.com/api/pc/getChapterContent?data={data}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            async with aiofiles.open("novel/" + title, mode="w", encoding="utf-8")as f:
                await f.write(dic['data']['novel']['content'])


if __name__ == '__main__':
    b_id = "4356290733"
    url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + b_id + '"}'
    asyncio.run(getCatalog(url))

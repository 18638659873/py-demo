# 使用异步 获取图片 requests.get() 是阻塞获取的
# 安装 pip insatll aiohttp
import asyncio
import aiohttp

urls = [
    "http://kr.shanghai-jiuxin.com/file/bizhi/20220928/jydbj5knlcv.jpg",
    "http://kr.shanghai-jiuxin.com/file/bizhi/20220928/mlx0fbnerwq.jpg",
    "http://kr.shanghai-jiuxin.com/file/bizhi/20220928/535ubypguwc.jpg"
]


async def download(url):
    name = url.rsplit("/", 1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open("img/" + name, mode="wb") as f:
                f.write(await resp.content.read())

    print(name, "over")


async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(download(url)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())

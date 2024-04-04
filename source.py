import asyncio

import aiohttp


async def source_from_anti_porn() -> set:
    url = 'https://raw.githubusercontent.com/4skinSkywalker/Anti-Porn-HOSTS-File/master/HOSTS.txt'
    filename = 'HOSTS.txt'
    await fetch_and_save_file(url, filename)
    print(f"File downloaded as {filename}")
    result = set()
    with open(filename, 'r') as f:
        readlines = f.readlines()
        for line in readlines:
            line = line.replace("0.0.0.0    ",'')
            line = line.replace('\n', '')
            result.add(line)
    return result


async def fetch_and_save_file(url, filename):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open(filename, 'wb') as file:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    file.write(chunk)


if __name__ == '__main__':
    asyncio.run(source_from_anti_porn())

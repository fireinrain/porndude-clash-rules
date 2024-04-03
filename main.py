import asyncio

import aiohttp

porndude_sites = ['https://theporndude.vip/',
                  'https://pornsites.com/', 'https://porngeek.com/']


async def fetch_index_page(url: str) -> {}:
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Referer': 'https://www.google.com/'
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                resp = await response.text()
                print(resp)
                return {'url': url, 'data': resp}
            else:
                error = ValueError(f"Failed to fetch data from {url}, status code: {response.status}")
                return {'url': url, 'data': error}


async def fetch_multiple_urls(urls):
    tasks = [fetch_index_page(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results


def extract_url_from_pornsites(page_str: str) -> []:
    pass

def extract_url_from_theporndude(page_str: str) -> []:
    pass

def extract_url_from_porngeek(page_str: str) -> []:
    pass


def extract_dynamic_resource(page_str: str) -> []:
    # the porndude 默认只有一部分是静态页面展示网址
    # 还有一部分是靠js加在出来
    # <script type="text/javascript" src="https://theporndude.com/includes/pi/en.1712086370.passive.info.js"></script>
    # var passive_skip_data = [];
    # var passive_index_file = 'en.1712086370.passive.idx.json';
    # var passive_index_cat_file = 'en.1712086370.passive.mobi.cat.json';
    # var passive_index_mobi_files = ['en.1712086370.passive.mobi.0.json','en.1712086370.passive.mobi.1.json','en.1712086370.passive.mobi.2.json','en.1712086370.passive.mobi.3.json','en.1712086370.passive.mobi.4.json','en.1712086370.passive.mobi.5.json','en.1712086370.passive.mobi.6.json','en.1712086370.passive.mobi.7.json','en.1712086370.passive.mobi.8.json','en.1712086370.passive.mobi.9.json','en.1712086370.passive.mobi.10.json'];
    # 但是目前通过header + cookie的方式无法访问到默认的页面
    # 默认页面上了cloudflare cdn 无法直接请求
    # 这部分暂不实现
    pass


def generate_clash_rules(sites: []):
    # 默认使用DOMAIN-SUFFIX 来匹配域名
    pass


async def main():
    pornsites_resp = await fetch_multiple_urls(porndude_sites)
    all_site = []
    for site in pornsites_resp:
        if 'theporndude' in site['url']:
            urls = extract_url_from_theporndude(site['data'])
            all_site.append(urls)
            continue
        if 'porngeek' in site['url']:
            urls = extract_url_from_porngeek(site['data'])
            all_site.append(urls)
            continue
        if '' in site['url']:
            urls = extract_url_from_pornsites(site['data'])
            all_site.append(urls)

    generate_clash_rules(all_site)



if __name__ == '__main__':
    asyncio.run(main())

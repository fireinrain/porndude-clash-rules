import asyncio
from urllib.parse import urlparse

import aiohttp
from bs4 import BeautifulSoup
porndude_sites = ['https://theporndude.vip',
                  'https://pornsites.com', 'https://porngeek.com']


async def fetch_index_page(url: str) -> {}:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                resp = await response.text()
                # print(resp)
                return {'url': url, 'data': resp}
            else:
                error = ValueError(f"Failed to fetch data from {url}, status code: {response.status}")
                return {'url': url, 'data': error}


async def fetch_multiple_urls(urls):
    tasks = [fetch_index_page(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results


async def extract_url_from_pornsites(link: str, page_str: str) -> []:
    soup = BeautifulSoup(page_str, 'html.parser')
    find_all = soup.find_all('a')
    site_urls = []
    for i in find_all:
        href = i.get('href')
        if '/review/' in href:
            continue
        if 'https://' in href:
            continue
        if '/' == href:
            continue
        if '/blog' == href:
            continue
        if '/' == href:
            continue
        if '/about' == href:
            continue
        if '/terms' == href:
            continue
        if '/privacy' == href:
            continue
        if '/disclaimer' == href:
            continue
        print(href)
        site_urls.append(href)
    results = []
    for url in site_urls:
        part_sites = f'{link}{url}'
        collect_page = await fetch_index_page(part_sites)
        beautiful_soup = BeautifulSoup(collect_page['data'], 'html.parser')
        all_site_div = beautiful_soup.find_all('a')
        await asyncio.sleep(3)
        print(all_site_div)
    await asyncio.sleep(0.01)
    return results


async def extract_url_from_theporndude(link: str, page_str: str) -> []:
    results = []

    soup = BeautifulSoup(page_str, 'html.parser')
    find_all = soup.find_all('a')
    site_urls = []
    for i in find_all:
        href = i.get('href')
        if '/review/' in href:
            continue
        if 'https://' or 'http' in href:
            parsed_url = urlparse(href)
            domain = parsed_url.netloc
            results.append(domain)
            continue
        if '/' == href:
            continue
        if '/blog' == href:
            continue
        if '/' == href:
            continue
        if '/about' == href:
            continue
        if '/terms' == href:
            continue
        if '/privacy' == href:
            continue
        if '/disclaimer' == href:
            continue
        print(href)
        site_urls.append(href)
    # for url in site_urls:
    #     part_sites = f'{link}{url}'
    #     collect_page = await fetch_index_page(part_sites)
    #     beautiful_soup = BeautifulSoup(collect_page['data'], 'html.parser')
    #     all_site_div = beautiful_soup.find_all('a')
    #     await asyncio.sleep(3)
    #     print(all_site_div)
    # await asyncio.sleep(0.01)
    return results


def extract_url_from_porngeek(link: str, page_str: str) -> []:
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
            urls = await extract_url_from_theporndude(site['url'], site['data'])
            all_site.append(urls)
            continue
        if 'porngeek' in site['url']:
            urls = extract_url_from_porngeek(site['url'], site['data'])
            all_site.append(urls)
            continue
        if 'pornsites' in site['url']:
            pass
            # urls = await extract_url_from_pornsites(site['url'], site['data'])
            # all_site.append(urls)

    generate_clash_rules(all_site)


if __name__ == '__main__':
    asyncio.run(main())
    # from urllib.parse import urlparse
    #
    #
    # def get_domain_from_url(url):
    #     parsed_url = urlparse(url)
    #     domain = parsed_url.netloc
    #     return domain
    #
    #
    # # Example usage:
    # url = 'https://www.example.com/path/to/page'
    # domain = get_domain_from_url(url)
    # print("Domain:", domain)

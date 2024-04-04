import asyncio
from urllib.parse import urlparse

import aiohttp
from bs4 import BeautifulSoup

import asyncio
from urllib.parse import urlparse
import aiohttp
from bs4 import BeautifulSoup
from source import source_from_anti_porn


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


async def fetch_redirected_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, allow_redirects=True, headers=headers) as response:
                return response.url
        except Exception as e:
            print(f"获取跳转链接异常: {e}")
            return None


async def main():
    sites_ = await fetch_index_page("https://theporndude.vip")
    # print(sites_)
    soup = BeautifulSoup(sites_['data'], 'html.parser')

    a_tags = soup.find_all('a')
    target_links = []
    for a in a_tags:
        href = a.get('href')
        # make http to https
        if 'https://' in href:
            target_links.append(href)
            continue
        if 'http://' in href:
            new_href = href.replace('http://', 'https://')
            target_links.append(new_href)
            continue
        # print(href)
    print(f"源链接数量: {len(a_tags)}")
    print(f"处理后的连接数量: {len(target_links)}")
    # print(all_site_div)

    # 先进行去重处理
    s = set(target_links)
    all_links = list(s)
    print(f"去重后的连接数量: {len(s)}")

    domain_sets = set()
    url_size = len(all_links)
    for index, link in enumerate(all_links):
        print(f"正在处理第{index + 1} 个链接, 还有: {url_size - index - 1},共有: {url_size}个链接...")
        parsed_url = urlparse(link)
        domain = parsed_url.netloc
        if domain == 'theporndude.vip':
            # 需要二次请求获取302跳转的地址
            real_link = await fetch_redirected_url(link)
            if real_link is None:
                continue
            await asyncio.sleep(0.2)
            resp_data = await fetch_index_page(str(real_link))
            soup = BeautifulSoup(resp_data['data'], 'html.parser')
            aa_tags = soup.find_all('a')
            for aa in aa_tags:
                href = aa.get('href')
                # make http to https
                if href is not None and 'https://' in href:
                    parsed_url = urlparse(href)
                    domain = parsed_url.netloc
                    domain_sets.add(domain)
                    continue
                if href is not None and 'http://' in href:
                    new_href = href.replace('http://', 'https://')
                    parsed_url = urlparse(new_href)
                    domain = parsed_url.netloc
                    domain_sets.add(domain)
                    continue
        else:
            # 直接加入domain 列表
            domain_sets.add(domain)
        print(f'当前已获得域名数量: {len(domain_sets)}')
    # write domain set to a text file
    cn_sets = await add_porndude_zh('PornDude-zh.html')
    domain_sets += cn_sets
    anti_set = await source_from_anti_porn()
    domain_sets += anti_set
    generate_clash_rule('porndude.txt', list(domain_sets))
    print(f"clash 规则生成完成")


async def add_porndude_zh(html_file: str) -> set:
    with open(html_file, 'r+') as f:
        html_content = f.read()
        soup = BeautifulSoup(html_content, 'html.parser')

        a_tags = soup.find_all('a')
        target_links = []
        for a in a_tags:
            href = a.get('href')
            # make http to https
            if href is not None and 'https://' in href:
                target_links.append(href)
                continue
            if href is not None and 'http://' in href:
                new_href = href.replace('http://', 'https://')
                target_links.append(new_href)
        print(f"源链接数量: {len(a_tags)}")
        print(f"处理后的连接数量: {len(target_links)}")
        # 去除重复
        # 先进行去重处理
        s = set(target_links)
        all_links = list(s)
        print(f"去重后的连接数量: {len(s)}")
        print(all_links)

        domain_sets = set()
        url_size = len(all_links)
        for index, link in enumerate(all_links):
            print(f"正在处理第{index + 1} 个链接, 还有: {url_size - index - 1},共有: {url_size}个链接...")
            parsed_url = urlparse(link)
            domain = parsed_url.netloc
            if domain == 'porndude.link':
                # 需要二次请求获取302跳转的地址
                real_link = await fetch_redirected_url(link)
                if real_link is None:
                    continue
                print(f"重定向到：{real_link}")
                await asyncio.sleep(0.2)
                domain = real_link.raw_host
                domain_sets.add(domain)
                continue
            if domain == 'theporndude.com':
                # TODO fetch site and parse site url
                # print(f"当前链接: {link}")
                continue
            else:
                # 直接加入domain 列表
                domain_sets.add(domain)

            print(f'当前已获得域名数量: {len(domain_sets)}')
    return domain_sets


def generate_clash_rule(file_name: str, domains: []):
    results = []
    result_rules = []
    for domain in domains:
        domain_split = domain.split('.')
        size = len(domain_split)
        if size == 2:
            results.append(domain)
            result_rules.append(f"  - '+.{domain}'")
            continue
        if size == 3:
            dm = domain_split[-2] + '.' + domain_split[-1]
            results.append(dm)
            result_rules.append(f"  - '+.{dm}'")
            continue
        dm = domain_split[-2] + '.' + domain_split[-1]
        results.append(dm)
        result_rules.append(f"  - '+.{dm}'")

    # payload:
    # - '+.265.com'
    clash_rules_str = '\n'.join(result_rules)
    rules_str = 'payload:\n'
    with open(file_name, 'w+') as f:
        f.write(rules_str + clash_rules_str)
        f.flush()


if __name__ == '__main__':
    # asyncio.run(main())
    asyncio.run(add_porndude_zh('PornDude-zh.html'))

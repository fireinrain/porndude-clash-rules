import requests

porndude_sites = ['https://theporndude.vip/',
                  'https://pornsites.com/', 'https://porngeek.com/']


def fetch_index_page(url: str) -> str:
    index_url = url
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Referer': 'https://www.google.com/'
    }
    resp = requests.get(index_url, headers=headers)
    resp.raise_for_status()

    print(resp.text)


def extract_static_resource(page_str: str) -> []:

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


if __name__ == '__main__':

    fetch_index_page("https://pornsites.com/")

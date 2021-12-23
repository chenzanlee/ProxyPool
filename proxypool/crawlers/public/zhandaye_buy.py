from proxypool.schemas.proxy import Proxy
import re

from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy


class ZhanDaYeBuy(BaseCrawler):
    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }
    urls = ['http://www.zdopen.com/PrivateProxy/GetIP/?api=202112231751318012&akey=e557eaeee9293d85&count=2&type=1']
    ignore = True

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        html = html + '\r\n'
        ip_address = re.compile('([\d:\.]*).*?\r\n')
        hosts_ports = ip_address.findall(html)
        for addr in hosts_ports:
            addr_split = addr.split(':')
            if (len(addr_split) == 2):
                host = addr_split[0]
                port = addr_split[1]
                yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = ZhanDaYeBuy()
    # for proxy in crawler.crawl():
    #     print(proxy)
    html = '223.214.70.132:33504\r\n223.198.243.43:26174'
    proxys = crawler.parse(html)
    for proxy in proxys:
        print(proxy)
# 223.214.70.132:33504
# 223.198.243.43:26174
# 223.214.70.132:33504

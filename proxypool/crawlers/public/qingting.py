from proxypool.schemas.proxy import Proxy
import re

from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy


class QingTingCrawler(BaseCrawler):

    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }
    urls = ['https://proxyapi.horocn.com/api/v2/proxies?order_id=9JWS1719924234723861&num=2&format=text&line_separator=win&can_repeat=yes&user_token=ab03fbfbbce6640f6b73f892b0e38356']
    ignore = True

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        ip_address = re.compile('([\d:\.]*).*?\r\n')
        hosts_ports = ip_address.findall(html)
        for addr in hosts_ports:
            addr_split = addr.split(':')
            if (len(addr_split) == 2):
                host = addr_split[0]
                port = addr_split[1]
                yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = QingTingCrawler()
    for proxy in crawler.crawl():
        print(proxy)

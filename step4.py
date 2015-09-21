# -*- coding: utf-8 -*-
import re
from collections import defaultdict


def parse_nginx_api(filename, limit):
    text = str(open(filename).readlines())
    regex = re.compile(r'(\d+\.\d+.\d+\.\d+)\s+-\s+-\s+', re.IGNORECASE | re.MULTILINE)
    list_ip = list(re.findall(regex, text))
    dict_ip = defaultdict(int)

    for ip in list_ip:
        dict_ip[ip] += 1

    return sorted(dict_ip.items(), key=(lambda x: x[1]), reverse=True)[:limit]


if __name__ == '__main__':
    print(parse_nginx_api('nginx.log', 10))

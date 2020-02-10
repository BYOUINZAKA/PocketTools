import re

from pandas import DataFrame


def get_date(url: str):
    if url.find('https://www.smogon.com/stats/') == -1:
        return None
    else:
        i = len(str('https://www.smogon.com/stats/'))
        _url = url[i:]
        j = (_url).find('/')
        return _url[:j] 


def get_mode(url: str):
    if url.rfind('.txt') == -1:
        return None
    else:
        pa = re.compile(r'.+[/](\S+?)[-]')
        return pa.findall(url)


def get_score(url: str):
    if url.rfind('.txt') == -1:
        return None
    else:
        pa = re.compile(r'[-](\d+?)[.]')
        return pa.findall(url)


def split_data(text: str):
    lines = re.split(r'[\n]', text)
    pa = re.compile(
        r'^\s[|]\s*(\d+)\s*[|]\s*(.+?)\s*[|]\s*(\S+[%])\s*[|].+[|]\s$')
    list = []
    for l in lines:
        result = pa.findall(l)
        if len(result) != 0:
            list.append(result[0])
    return list

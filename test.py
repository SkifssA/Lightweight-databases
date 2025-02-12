import requests
from bs4 import BeautifulSoup

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'ru,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Cookie': '__ddg1_=p1eIQPotO9KojddL1XD6; device_view=full; PHPSESSID=s0tf8d49kbnkpd9rh2kqhipr9o; __ddg9_=146.185.233.56; __ddg10_=1739282430; __ddg8_=Tb1a3892mKxlPnsp',
    'Pragma': 'no-cache',
    'Priority': 'u=0, i',
    'Referer': 'https://yandex.ru/',
    'Sec-Ch-Ua': '"Chromium";v="130", "YaBrowser";v="24.12", "Not?A_Brand";v="99", "Yowser";v="2.5"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36'
}
url = 'https://animego.me/anime/keyon-a2512'

html = requests.get(url, headers=headers).text

# Создаем объект BeautifulSoup для парсинга HTML
soup = BeautifulSoup(html, 'html.parser')
data = {}
for i in soup.find_all(class_='anime-title'):
    data['name'] = i.find('h1').text
for i in soup.find_all(class_='rating-value'):
    data['score'] = i.text
for i in soup.find_all(id='video-watch2'):
    w = []
    for j in i.find_all(class_='seasons-item col-6 col-sm-4 col-md-4 col-lg-3 mb-3'):
        a = j.find('a')
        url = a.get('href')
        url = url[:url.rfind('-')] + '-a' + url[url.rfind('-') + 1:]
        w.append((url, a.text.strip(), j.find(class_='seasons-item-info text-gray-dark-5 small').text.strip()))
    data['linked'] = w
    print(data)
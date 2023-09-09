# import requests
# from bs4 import BeautifulSoup
#
#
# class Parser:
#     html = ""
#     res = []
#
#     def __init__(self, url, path):
#         self.url = url
#         self.path = path
#
#     def get_html(self):
#         # print(requests.get(self.url).text)
#         req = requests.get(self.url).text
#         self.html = BeautifulSoup(req, 'lxml')
#
#     def parsing(self):
#         news = self.html.find_all('div', class_="caption")
#         for item in news:
#             title = item.find("h3").text
#             href = item.find('a').get('href')
#             author = item.find('a', class_='topic-info-author-link').text.strip()
#             self.res.append({
#                 'title': title,
#                 'href': href,
#                 'author': author
#             })
#
#     def save(self):
#         print(self.res)
#         with open(self.path, 'w') as f:
#             i = 1
#             for item in self.res:
#                 f.write(f"Новость № {i}\n\n Название: {item['title']}\nСсылка {item['href']}\n {item['author']}"
#                         f"\n\n{'*' * 20}\n")
#                 i += 1
#
#     def run(self):
#         self.get_html()
#         self.parsing()
#         self.save()


import requests
from bs4 import BeautifulSoup


class Parser:
    html = ""
    res = []
    item = ''

    def __init__(self, url, path):
        self.url = url
        self.path = path
        self.i = 0
        self.news = []
        self.title = ''
        self.short_text = ''
        self.y = 0

    def get_html(self):
        self.i += 1
        href = self.item.find('a').get('href')
        ref = requests.get(href).text
        self.html = BeautifulSoup(ref, 'html.parser')

    def parsing(self):
        title = self.html.find('h1', class_='topic-title word-wrap').text
        short_text = self.html.find('div', class_='topic-content text').find('p').text
        # source = self.html.find('div', class_='topic-content text').find_all('p')[-1].find('a').get('href')
        self.title = f"title{self.i}"
        self.short_text = f"short_text{self.i}"
        self.res.append({
            # self.title: title,
            self.short_text: short_text,
            # f"'source{self.i}'": source,
        })

    def save(self):
        # print(self.res)
        with open(self.path, 'a') as f:
            for of in self.res:
                self.y += 1
                # s = f"title{self.y}"
                s1 = f"short_text{self.y}"
                f.write(f"Новость № {self.y} \n\n Содержание:  {of[s1]}\n\n\n")
                        # f"Начало статьи: {of[s1]}")

    def run(self):
        req = requests.get(self.url).text
        html = BeautifulSoup(req, 'html.parser')
        self.news = html.find_all('h3', class_="topic-title")
        for self.item in self.news:
            self.get_html()
            self.parsing()
        self.save()


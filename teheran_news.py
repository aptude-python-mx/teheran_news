from article import Article
from utilities import soup, change_topic_name
from itertools import islice

class Teheran_news(Article):

    def __init__(self, topic=None):
        self.tp = topic
        self.num = 0

    @classmethod
    def pages(cls, list_link):
        res_link = []
        for link in list_link:
            the_soup = soup(link)
            date = the_soup.find("span", {"class": "item-item ltr"})
            img = the_soup.find(class_="third-news")

            for link in img.find_all('a', href=True): 
                full_link = 'https://www.tehrantimes.com' + link['href']
                if full_link not in res_link: 
                    res_link.append(full_link)
        return res_link

    @property
    def info(self):
        the_topic = change_topic_name(self.tp)
        pre_list = []
        info_list = []
        page_news = 0

        while True:
            self.num += 1
            if self.num % 30 == 1:
                page_news += 1
                if the_topic == None:
                    prelink = 'https://www.tehrantimes.com/page/archive.xhtml?wide=0&ms=0&pi={}'.format(page_news)
                else:
                    prelink = 'https://www.tehrantimes.com/page/archive.xhtml?wide=0&ms=0&pi={}&tp={}'.format(page_news,the_topic)
                the_urls = self.pages([prelink])
                if not the_urls:
                    print("Is the end of the news")
                    break
                else:
                    for url in the_urls:
                        try:
                            info_list.append(self.parse_info(url))
                        except AttributeError:
                            pass

            for the_news in info_list:
                yield the_news
                info_list = []

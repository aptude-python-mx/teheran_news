import datetime
from objectview import Objectview
from itertools import islice
from utilities import soup

class Article:
    
    def get_dict(self, list):
        names = ['topic', 'author', 'title', 'created_at', 'text', 'related_news', 'tags']
        return(dict(zip(names, list)))

    def parse_info(self, link):
        the_soup = soup(link)

        #topic
        category = the_soup.find(class_="breadcrumb")
        topic = category.find('li')

        #author
        author = the_soup.find("div", {"class": "kicker", "itemprop": "alternativeHeadline"})
        try:
            the_author = author.text
        except AttributeError:
            the_author = None

        #title
        title = the_soup.find("h2", {"class": "item-title", "itemprop": "headline"})

        #created_at
        date_soup = the_soup.find("div", {"class": "item-date half-left"})
        created_at = datetime.datetime.strptime( date_soup.text, '%B %d, %Y - %H:%M' )

        #text
        text = the_soup.find("div", {"class": "item-text"})

        #related_news
        related = the_soup.find(class_="box list header-clean related-items")
        related_news = []
        try:
            enlaces = related.find_all('li')
            for enlace in enlaces:
                related_news.append(enlace.text)
        except:
            related_news.append(None)
        
        #tags
        get_tags = the_soup.find(class_="box list-clean header-clean list-inline list-tags tags")
        enlaces = get_tags.find_all('li')
        tags = []
        for enlace in enlaces:
            tags.append(enlace.text)

        data_list = [topic.text, the_author, title.text, created_at, text.text, related_news, tags]
        data_dict = self.get_dict(data_list)
        data_obj = Objectview(data_dict)
        return data_obj

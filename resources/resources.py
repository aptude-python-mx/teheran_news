import requests
from bs4 import BeautifulSoup
import pprint


class Resources():

    @classmethod
    def soup_resource(cls, links):
        request  = requests.get(links)
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        return soup

    @classmethod
    def link_resource(cls, links):
        soup = cls.soup_resource(links)
        
        img = soup.find(class_="third-news")
        res = []
        for i in img.find_all('a', href=True):
            full_link = 'https://www.tehrantimes.com' + i['href']
            if full_link not in res: 
                res.append(full_link) 
        return(res)

    @classmethod
    def element_resource(cls, links):
        soup = cls.soup_resource(links)

        #topic
        res = []
        category = soup.find(class_="breadcrumb")
        enlaces = category.find('li')
        for enlace in enlaces:
            res.append(enlace.text)

        #author
        author = soup.find("div", {"class": "kicker", "itemprop": "alternativeHeadline"})
        try:
            res.append(author.text)
        except:
            res.append('')

        #title
        title = soup.find("h2", {"class": "item-title", "itemprop": "headline"})
        res.append(title.text)

        #date
        date = soup.find("div", {"class": "item-date half-left"})
        res.append(date.text)

        #image
        img = soup.find("figure", {"class": "item-img"})
        for a in img.find_all('a', href=True):
            res.append(a['href'])

        #text
        text = soup.find("div", {"class": "item-text"})
        res.append(text.text)

        #related_news
        related = soup.find(class_="box list header-clean related-items")
        related_list = []
        try:
            enlaces = related.find_all('li')
            for enlace in enlaces:
                related_list.append(enlace.text)
        except:
            related_list.append('')
        res.append(related_list)

        #tags
        tags = soup.find(class_="box list-clean header-clean list-inline list-tags tags")
        enlaces = tags.find_all('li')
        tags_list = []
        for enlace in enlaces:
            tags_list.append(enlace.text)
        res.append(tags_list)
        return res

    @classmethod
    def preview_resource(cls, links):
        soup = cls.soup_resource(links)

        date = soup.find("span", {"class": "item-item ltr"})
        img = soup.find(class_="third-news")

        res_link = []
        res_date = []
        res_title = []
        res_text = []

        # Title
        for title in img.find_all('h3'): 
                res_title.append(title.text)

        # Date
        for date in img.find_all('span'):  
            try:
                res_date.append(date['title'])
            except:
                continue

        #Link
        for link in img.find_all('a', href=True): 
            full_link = 'https://www.tehrantimes.com' + link['href']
            if full_link not in res_link: 
                res_link.append(full_link)

        # Text
        for text in img.find_all('p'): 
                res_text.append(text.text)

        results = list(zip(res_title,res_date,res_link,res_text))
        list_results = [list(elem) for elem in results]
        return list_results

    @classmethod
    def change_kwargs_name(cls, kwargs):
        try:
            if kwargs['tp'] == 'Society' or kwargs['tp'] == 'society':
                kwargs['tp'] = '696'
            elif kwargs['tp'] == 'Economy' or kwargs['tp'] == 'economy':
                kwargs['tp'] = '697'
            elif kwargs['tp'] == 'Politics' or kwargs['tp'] == 'politics':
                kwargs['tp'] = '698'
            elif kwargs['tp'] == 'Sports' or kwargs['tp'] == 'sports':
                kwargs['tp'] = '699'
            elif kwargs['tp'] == 'Culture' or kwargs['tp'] == 'culture':
                kwargs['tp'] = '700'
            elif kwargs['tp'] == 'International' or kwargs['tp'] == 'international':
                kwargs['tp'] = '702'
            else:
                return print("Topic {} doesn't exist".format(kwargs['tp']))
        except:
            pass
        return kwargs

    @classmethod
    def pretty(cls, data):
        pp = pprint.PrettyPrinter(indent=4)
        return pp.pprint(data)
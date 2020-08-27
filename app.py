from scrapper import Get_news
import pprint
from resources.resources import Resources

pprint = Resources()
news = Get_news()

#Test get_links
"""links = news.get_links("https://www.tehrantimes.com/page/archive.xhtml?wide=0&ms=0&pi=2&tp=697")
#links = news.get_links("https://www.tehrantimes.com/archive?tp=697", 
#                       "https://www.tehrantimes.com/page/archive.xhtml?wide=0&ms=0&pi=2",
#                       "https://www.tehrantimes.com/page/archive.xhtml?wide=0&ms=0&pi=3&tp=696")
#print(links)
pprint.pretty(links)"""

#Test get_elements
"""elements = news.get_elements("https://www.tehrantimes.com/news/451619/Medicinal-plants-hold-potential-for-realizing-surge-in-production")
#elements = news.get_elements("https://www.tehrantimes.com/news/451525/A-glimpse-of-Muharram-mourning-rituals-across-Iran-Bil-Zani",
#                             "https://www.tehrantimes.com/news/451659/Energy-efficient-households-to-get-100-discount-on-electricity",
#                             "https://www.tehrantimes.com/news/451604/Incentive-packages-help-energy-ministry-pass-summer-without-blackouts")
#print(elements)
pprint.pretty(elements)"""

#Test get_previews
"""previews = news.get_previews("https://www.tehrantimes.com/page/archive.xhtml?wide=0&ms=0&pi=2",
                             "https://www.tehrantimes.com/archive?tp=697")

#previews = news.get_previews(pi=1,tp='Politics',ms=0,dy=10,mn=2,yr=2019)
#previews = news.get_previews(pi=4,tp='sports',mn=5,yr=2020)
#print(previews)
pprint.pretty(previews)"""


#Test finder
"""keyword_list = ['Development','Plan','Persian','Zataria'] # If it prints an empty list maybe is because the news that contains these words are in another page
news_to_find = news.find(keyword_list, pi=2, tp='Society')
#pprint.pretty(previews)
print(news_to_find)"""
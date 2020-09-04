from teheran_news import Teheran_news
from itertools import islice

"""articles = Teheran_news('Politics')
for news in islice(articles.info, 32):
    print(news.title, news.created_at)"""

articles = Teheran_news()
for news in islice(articles.info, 100):
    print(news.topic, news.title, news.created_at)

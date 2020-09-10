from teheran_news import Teheran_news
from itertools import islice


# Get 32 news of politics

articles = Teheran_news('Politics')
for news in islice(articles.info, 32):
    print(news.title, news.created_at)

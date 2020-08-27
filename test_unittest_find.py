import unittest
from scrapper import Get_news


class TestFind(unittest.TestCase):

    def setUp(self):
        news = Get_news()

        keyword_list = ['Development','Plan','Persian','Zataria'] # If it prints an empty list maybe is because the news that contains these words are in another page
        self.test_news_to_find = news.find(keyword_list, pi=2, tp='Society')

    def tearDown(self):
        pass

    #Test find
    def test_find_first_len(self):
        previews_size = 8
        self.assertEqual(len(self.test_news_to_find[0]), previews_size)

if __name__ == '__main__':
    unittest.main()
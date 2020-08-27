import unittest
from scrapper import Get_news


class TestScrapper(unittest.TestCase):

    def setUp(self):
        news = Get_news()

        self.test_news_links = news.get_links("https://www.tehrantimes.com/page/archive.xhtml?wide=0&ms=0&pi=2&tp=697")
        self.test_news_elements = news.get_elements("https://www.tehrantimes.com/news/451525/A-glimpse-of-Muharram-mourning-rituals-across-Iran-Bil-Zani")
        self.test_news_previews = news.get_previews("https://www.tehrantimes.com/page/archive.xhtml?wide=0&ms=0&pi=3&tp=702")

    def tearDown(self):
        pass

    #Test get_links
    def test_links_len(self):
        links_size = 30
        self.assertEqual(len(self.test_news_links[0]), links_size)

    def to_test_loop(self, the_list):
        for i in the_list:
            for j in i:
                self.assertTrue((j).startswith('https://www.tehrantimes.com/'))

    def test_linktrue(self):
        self.to_test_loop(self.test_news_links)
    
    #Test get_elements
    def test_elements_len(self):
        elements_size = 8
        self.assertEqual(len(self.test_news_elements[0]), elements_size)

    #Test get_previews
    def test_previews_len(self):
        previews_size = 30
        self.assertEqual(len(self.test_news_previews[0]), previews_size)

    def to_test_prev_len(self, the_list):
        previews_size = 4
        for i in the_list:
            for j in i:
                self.assertEqual(len(j), previews_size)
    
    def test_linktrue(self):
        self.to_test_prev_len(self.test_news_previews)


if __name__ == '__main__':
    unittest.main()
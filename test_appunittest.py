import unittest
from scrapper import Get_news

class TestScrapper(unittest.TestCase):

    def setUp(self):
        news_1 = Get_news()
        news_2 = Get_news()
        news_3 = Get_news()

        self.test_news_links_1 = news_1.get_links("https://www.tehrantimes.com/page/archive.xhtml?wide=0&ms=0&pi=7&tp=698")
        self.test_news_links_2 = news_2.get_links("https://www.tehrantimes.com/page/archive.xhtml?mn=1&wide=0&ms=0&pi=2")
        self.test_news_links_3 = news_3.get_links("https://www.tehrantimes.com/archive?pi=1&tp=699&ms=0&mn=1")

        self.test_news_elements_1 = news_1.get_elements("https://www.tehrantimes.com/news/451650/VAR-to-be-used-in-ACL-from-quarters")
        self.test_news_elements_2 = news_2.get_elements("https://www.tehrantimes.com/news/451689/Daesh-would-have-reached-heart-of-Europe-without-Gen-Soleimani")
        self.test_news_elements_3 = news_3.get_elements("https://www.tehrantimes.com/news/451679/Iranian-airports-among-best-in-West-Asia-and-Africa-region")

        self.test_news_previews_1 = news_1.get_previews("https://www.tehrantimes.com/page/archive.xhtml?wide=0&ms=0&pi=7&tp=698")
        self.test_news_previews_2 = news_2.get_previews("https://www.tehrantimes.com/page/archive.xhtml?mn=1&wide=0&ms=0&pi=2")
        self.test_news_previews_3 = news_3.get_previews(pi=1,tp='sports',mn=5,yr=2020)

    def tearDown(self):
        pass

    #Test get_links
    def test_links_len(self):
        links_size = 30
        self.assertEqual(len(self.test_news_links_1[0]), links_size)
        self.assertEqual(len(self.test_news_links_2[0]), links_size)
        self.assertEqual(len(self.test_news_links_3[0]), links_size)

    def to_test_loop(self, the_list):
        for i in the_list:
            for j in i:
                self.assertTrue((j).startswith('https://www.tehrantimes.com/'))

    def test_linktrue(self):

        self.to_test_loop(self.test_news_links_1)
        self.to_test_loop(self.test_news_links_2)
        self.to_test_loop(self.test_news_links_3)
    
    #Test get_elements
    def test_elements_len(self):
        elements_size = 8
        self.assertEqual(len(self.test_news_elements_1[0]), elements_size)
        self.assertEqual(len(self.test_news_elements_2[0]), elements_size)
        self.assertEqual(len(self.test_news_elements_3[0]), elements_size)

    #Test get_previews
    def test_previews_len(self):
        previews_size = 30
        self.assertEqual(len(self.test_news_previews_1[0]), previews_size)
        self.assertEqual(len(self.test_news_previews_2[0]), previews_size)
        self.assertEqual(len(self.test_news_previews_3[0]), previews_size)

    def to_test_prev_len(self, the_list):
        previews_size = 4
        for i in the_list:
            for j in i:
                self.assertEqual(len(j), previews_size)
    
    def test_linktrue(self):
        self.to_test_prev_len(self.test_news_previews_1)
        self.to_test_prev_len(self.test_news_previews_2)
        self.to_test_prev_len(self.test_news_previews_3)

if __name__ == '__main__':
    unittest.main()
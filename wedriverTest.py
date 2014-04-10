import unittest
from selenium import webdriver


class Test(unittest.TestCase):
	def setUp(self):
		self.chrome=webdriver.Chrome()
		
	def tearDown(self):
		pass
		# self.chrome.quit()

	def _searchInBaidu(self,url='http://www.baidu.com',keyword='abcd'):
		self.chrome.get(url)
		input = self.chrome.find_element_by_id('kw')
		input.send_keys(keyword)
		button = self.chrome.find_element_by_id('su')
		button.submit()
		
	def testBaidu(self):
		self._searchInBaidu()
		
		
		
		
if __name__ == "__main__":
	unittest.main()
	
		
		


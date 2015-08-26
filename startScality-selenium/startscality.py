from selenium import webdriver
import time, platform
from sys import argv

class start_scality():
	def __init__(self):
		if 'indows' in platform.system():
			self.browser=webdriver.Chrome()
		else:
			self.browser=webdriver.Firefox()
		
	def get_page(self,url):
		self.browser.get(url)
	
	def input_xpath(self, xpath, value, index=0):
		element = self.browser.find_elements_by_xpath(xpath)[index]
		print 'find the element ' + xpath
		element.clear()
		element.send_keys(value)
		
	def submit_xpath(self, xpath,index=0):
		button = self.browser.find_elements_by_xpath(xpath)[index]
		print 'find the button '+xpath
		button.submit()
	
	def click_xpath(self, xpath,index=0):
		button = self.browser.find_elements_by_xpath(xpath)[index]
		print 'find the button '+xpath
		button.click()
	
	def close_quit(self):
		self.browser.close()
	
if __name__ == '__main__':
	try:
		test = start_scality()

		ip = argv[1]
		test.get_page('http://%s:3080/login/'%ip)
		test.input_xpath(xpath="//input[@name='username']", value='root')
		test.input_xpath(xpath="//input[@name='password']", value='admin')
		test.submit_xpath(xpath="//input[@type='submit']")

		
		if '126' in str(ip):
			path = 'scalityRing'
		elif '129' in str(ip):
			path = 'MXQA'
		
		test.get_page('http://%s:3080/sup/Local/%s/?&search=type:nodes'%(ip,path))
		for i in range(6):
			xpath = "//a[@href='node/%s:%s/0/join']"%(ip,str(8084+i))
			test.click_xpath(xpath)
			time.sleep(2)
		test.get_page('http://%s:3080/sup/Local/%s/?&search=type:nodes'%(ip,path))
		print 'Scality on '+ ip + ' started'
		test.close_quit()
	except:
		print 'Scality on '+ ip + ' already started'
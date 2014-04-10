from selenium import webdriver

class test():
	def login(self,url='http://btdantefe01.cpth.ie:60080/cp/ps/Main/login/accesstest',user='aui.user1'):
		self.chrome=webdriver.Chrome()
		self.chrome.get(url)
		inputUser = self.chrome.find_element_by_id('user')
		inputUser.clear()
		inputUser.send_keys(user)
		inputDomain = self.chrome.find_element_by_id('domain')
		inputDomain.clear()
		inputDomain.send_keys('qa.dom')
		inputPwd = self.chrome.find_element_by_id('password')
		inputPwd.clear()
		inputPwd.send_keys('password')
		button = self.chrome.find_element_by_id('login')
		button.submit()
		self.trHeader = self.chrome.find_elements_by_xpath("//tr[@class='x-grid-header-row']")
		self.tr = self.chrome.find_elements_by_xpath("//tr[@class='x-grid-row']")
	
if __name__ == '__main__':
        pass

import unittest
import time
from selenium import webdriver


class Test(unittest.TestCase):	#	
	def setUp(self):
		self.chrome=webdriver.Chrome()
		self.chrome.implicitly_wait(30)
		
	def tearDown(self):
		pass
		# self.chrome.quit()

	def _login(self,url='http://btdantefe01.cpth.ie:60080/cp/ps/Main/login/accesstest',user='aui.user1'):
		print 'login..'
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
		self.gridHeader = self.chrome.find_elements_by_xpath("//tr[@class='x-grid-header-row']")
		self.grid = self.chrome.find_elements_by_xpath("//tr[@class='x-grid-row']")
		
	def _verifyById(self):
		pass
			
	def _verifyBySpath(self):
		pass
		
	def _checkMails(self):
		print 'check mails..'
		self.mailIcons = self.chrome.find_elements_by_xpath("//td[@class=' x-grid-cell x-grid-cell-gridcolumn-1048   ']")
		boxes = self.chrome.find_elements_by_xpath("//td[@class=' x-grid-cell x-grid-cell-gridcolumn-1062  x-grid-cell-special x-grid-cell-row-checker x-grid-cell-first']")
		for box in boxes:
			box.click()
			
	def _mailAction(self,action='f'):
		print 'mail action'+action
		actionButton = self.chrome.find_element_by_id('button-1030-btnEl')
		actionButton.click()
		if 'f' in action:
			flagButton = self.chrome.find_element_by_id('menuitem-1032-itemEl')
			flagButton.click()
		elif 'r' in action()
			readButton = self.chrome.find_element_by_id('menuitem-1033-itemEl')
			readButton.click()
		elif 'unr' in action()
			unreadButton = self.chrome.find_element_by_id('menuitem-1034-itemEl')
			unreadButton.click()
			
	def _gotoCalendar(self):
		print 'go to Calendar..'
		calendarButton = self.chrome.find_element_by_id('CAL.appbutton-btnEl')
		calendarButton.click()


		
	def testAUI(self):
		self._login()
		self._checkMails()
		self._mailAction('f')
		# self._gotoCalendar()
		
		
		
		
if __name__ == "__main__":
	unittest.main()
		
		


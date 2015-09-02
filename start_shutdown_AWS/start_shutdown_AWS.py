from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions 
from selenium.webdriver.common.keys import Keys
from sys import exit
from time import sleep
from sys import argv
from datetime import datetime


def execute_action_on_single_vm(browser, vm_instance, action):
	
	#Set keyword in search field
	search_box=browser.find_element_by_xpath("//div[@class='AMB']/input[1]")
	search_box.send_keys(str(vm_instance))
	sleep(3)
	search_box.send_keys(Keys.ENTER)
	sleep(5)

	#Find and open Action menu
	buttons = browser.find_elements_by_xpath("//button")
	for btn in buttons:
		if btn.text == "Actions":
			btn.click()
			break
	sleep(3)

	#Go to instance state
        menuitems = browser.find_elements_by_xpath("//div[@role='menuitem']")
        for item in menuitems:
		if item.text == "Instance State":
			item.click()
			break
	sleep(3)        


	#Start instance
	if action == "start":
		starts=browser.find_elements_by_xpath("//div[@role='menuitem']")
		for start in starts:
			if start.text == "Start":
				start.click()
				break

		sleep(3)
		
		#Confirmation
		browser.find_element_by_xpath("//div[@class='dialogMiddleCenterInner dialogContent']/div/div[5]/div[1]/button[1]").click()
		sleep(3)
		browser.get_screenshot_as_file('./test_start.jpg')
	#Stop instance
	elif action == "stop":
		stops=browser.find_elements_by_xpath("//div[@role='menuitem']")
                for stop in stops:
                        if stop.text == "Stop":
                                stop.click()
                                break
		sleep(3)
		
		#Confirmation
		browser.find_element_by_xpath("//div[@class='dialogMiddleCenterInner dialogContent']/div/div[5]/div[1]/button[1]").click()
		sleep(3)
		browser.get_screenshot_as_file('./test_stop.jpg')
	print "%s has been executed on %s." % (action.upper(), vm_instance)

def execute_action_on_multi_vm(browser, vm_list, action):
	sleep(3)
	for vm in vm_list:
		execute_action_on_single_vm(browser, vm, action)
		
		#Clear keyword
		browser.find_element_by_xpath("//input[@placeholder='Add filter']").click()
		browser.find_element_by_xpath("//a[@title='Clear all']").click()

def execute_action_by_keyword(browser, keyword, action): #Pretty sure it's NOT working at the moment
	sleep(3)
	search_box=browser.find_element_by_xpath("//div[@class='FKB']/input[1]")
	search_box.send_keys('SBAI')
	search_box.send_keys(Keys.ENTER)
	#Select all
	browser.find_element_by_xpath("//div[@class='IFB']/label/span[1]").click()
	#Open action menu
	browser.find_element_by_xpath("//div[@class='O0C']/button[2]").click()

	if action == "start":
		browser.find_element_by_xpath("//div[@class='DLB']/div[25]").click()
		sleep(3)
		browser.find_element_by_xpath("//div[@class='dialogMiddleCenterInner dialogContent']/div/div[5]/div[1]/button[1]").click()
	elif action == "stop":
		browser.find_element_by_xpath("//div[@class='DLB']/div[24]").click()
		sleep(3)
		browser.find_element_by_xpath("//div[@class='dialogMiddleCenterInner dialogContent']/div/div[5]/div[1]/button[1]").click()

	print "The action of %s has been executed on the VMs with keyword of %s." % (action.upper(), keyword) 



if __name__ == '__main__':


	if len(argv) == 1:
		print "Go to normal mode."
		#Global variables
		option = ""
		single_vm_instance = ""
		multi_vms_list = ""
		expected_keyword = ""

		prompt = '''
		Please select from the following options(1-3):
		1. Single VM
		2. Multiple VMs
		3. VMs with specific keyword(Default: SBAI)
		4. Quit
		'''
		option = raw_input(prompt)	#Obviously, need a WHILE loop for CLI mode

		if int(option) not in range(1,4):
			print "Invali option!"
			exit(1)

		if option == "4":
			exit(0)
		elif option == "1":
			single_vm_instance = raw_input("Please provide vm instance ID: ")
		elif option == "2":
			# multi_vms_list = raw_input("Please provide vm instance IDs(separated by space): ")
			multi_vms_list = "i-7e8de020 i-708de02e i-718de02f i-7f8de021 i-835aff41"
			if len(multi_vms_list) == 0:
				print "Empty list can't be accepted. Please re-lanuch and try again."
				exit(1)
		elif option == "3":
			expected_keyword = raw_input("Please enter a keyword: ")
			if len(expected_keyword) == 0:
				print "It's too risk to execute any actions on all the VMs. Force to quit!"
				exit(1)

		# action = raw_input("Do you want to start or stop VM instances under SBAI(start/stop)?")
		action = "start"
		

		if action != "start" and action != "stop":
			print "Can't tell action you entered"
			exit(1)

	elif len(argv) >= 5:
		if argv[1] == "slient":
			option = argv[2]
			#Check action value
			if argv[3] == "start" or argv[3] == "stop":
				action = argv[3]
			else:
				print "Invalid action: %s" % argv[3]
				exit(1)
			#Check optionv value & data 
			if option == "1" and len(argv[4:]) == 1:
				single_vm_instance = argv[4:][0]
			elif option == "2" and len(argv[4:]) >= 2:
				multi_vms_list = argv[4:]
			elif option == "3" and len(argv[4:]) == 1:
				expected_keyword = argv[4:]
			else:
				print "Invalid option and data."
				exit(1)
		elif argv[1] == "debug":
			print argv[1], argv[2], argv[3], argv[4:][0]
			exit(0)	
	else:
		print "Invalid parameters."
		exit(1)

	#Start webdriver actions
	print "It's started @ %s" % datetime.now()
	browser = webdriver.Firefox()
	browser.get('https://messaging.signin.aws.amazon.com/console')
	browser.implicitly_wait(5)

	####################################
	# Login and go to instance mgmt page
	####################################

	# username = browser.find_element_by_id('username')
	# passwd = browser.find_element_by_id('password')
	username = "vwang"
	passwd = "opwvM5g779!"

	username.send_keys('')	#Provide AWS console's credential, or add support of reading from ENV_VAR
	passwd.send_keys('')	#Provide AWS console's credential, or add support of reading from ENV_VAR
	browser.find_element_by_id('signin_button').click()

	browser.get('https://console.aws.amazon.com/ec2/v2/home?region=us-west-1#Instances:')
	# Need a long wait here
	browser.implicitly_wait(300)


	#########################################
	# Start or Stop VM instances
	#########################################


	if option == "1":
		execute_action_on_single_vm(browser, single_vm_instance, action)
	elif option == "2":
		execute_action_on_multi_vm(browser, multi_vms_list, action)
	elif option == "3":
		execute_action_by_keyword(browser, expected_keyword, action)


	#################
	# Logout
	#################

	browser.find_element_by_xpath("//div[@id='nav-menu-right']/a[1]/div[1]").click()
	browser.find_element_by_xpath("//div[@id='awsc-username-menu-footer']/a[@id='aws-console-logout']").click()

	sleep(10)

	browser.implicitly_wait(20)

	browser.quit()
	print "It's finished %s." % datetime.now()

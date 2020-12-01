#Imports modules
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from config import keys
from authenticator import authentication_code
import time

#Sets chrome driver as active driver
driver = webdriver.Chrome('chromedriver')

#Logs into webapp and selects market tab
def login(k):
	#Fetches webapp url
	driver.get('https://www.ea.com/fifa/ultimate-team/web-app/')
	time.sleep(10)

	#Selects webapp login button and clicks
	login_button = driver.find_element_by_xpath('//*[@id="Login"]/div/div/button[1]')
	login_button.click()

	time.sleep(2)

	#Enters email from config file into email field
	email_field = driver.find_element_by_xpath('//*[@id="email"]')
	email_field.send_keys(k["email"])

	time.sleep(1)

	#Enters password from config file into password field
	password_field = driver.find_element_by_xpath('//*[@id="password"]')
	password_field.send_keys(k["password"])

	time.sleep(1)

	#Submits login form
	driver.find_element_by_xpath('//*[@id="btnLogin"]/span').click()
	
	time.sleep(1)

	#Sends security code to users email
	security_code_send = driver.find_element_by_xpath('//*[@id="btnSendCode"]/span')
	security_code_send.click()

	time.sleep(15)

	#Enters security code into field using authentication script
	security_code_field = driver.find_element_by_xpath('//*[@id="oneTimeCode"]')
	security_code_field.send_keys(authentication_code())

	time.sleep(1.5)

	#Submits security code form
	subit_security_code = driver.find_element_by_xpath('//*[@id="btnSubmit"]')
	subit_security_code.click()

	time.sleep(15)

	#Selects transer market tab from sidebar
	transfer_market_tab = driver.find_element_by_xpath('/html/body/main/section/nav/button[3]')
	transfer_market_tab.click()

	#Selects search transfer market button on screen
	search_market_button = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/div[2]/div[2]')
	search_market_button.click()

	#Asks user to enter player name, sniping price and selling price
	print("Enter player name in box...")

	snipe_price = input("MAX BIN Price: ")

	time.sleep(1)

	driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input').send_keys(snipe_price)
	time.sleep(1)


	#Calls sniping function
	snipe()

#Checks if player exists
def check_exists_by_xpath(xpath):
	try:
		driver.find_element_by_xpath(xpath)
	except NoSuchElementException:
		return False
	return True

def list_player():
	list_on_market = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[1]/button')
	list_on_market.click()

	time.sleep(5)
	
	listed = input("Press enter when card is listed")

	
#Snipes player on market
def snipe():
	while True:
		
		#Selects search button to search on market
		search_button = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]')
		search_button.click()

		time.sleep(0.75)

		#If player has popped up to buy
		if check_exists_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[1]/div/div[1]') == True:
			 #Selects player box 
			 time.sleep(0.2)
			 #driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[1]/button').click()
			
			 #Selects buy now button
			 buy_button = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]')
			 buy_button.click()

			 #Selects confirm buy button
			 buy_confirm = driver.find_element_by_xpath('/html/body/div[4]/section/div/div/button[1]')
			 buy_confirm.click()
			 
			 time.sleep(2)

			 list_player()
			 
		else:
			time.sleep(1)
			#Selects back button from market
			back_button = driver.find_element_by_xpath('/html/body/main/section/section/div[1]/button[1]')
			back_button.click()
			
			time.sleep(0.5)

			bid_min = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/button[2]')
			bid_min.click()

			time.sleep(0.5)

			
	
	


if __name__ == '__main__':
 	login(keys)
from selenium import webdriver

driver = webdriver.Chrome('/Users/Joseph/Downloads/chromedriver')  # Optional argument, if not specified will search path.

driver.get('http://www.youtube.com/');

#time.sleep(5) # Let the user actually see something!

searchbox = driver. find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys('you can do it')
searchbox.submit()

#time.sleep(5) # Let the user actually see something!

driver.quit()  
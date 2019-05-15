from selenium import webdriver

browser = webdriver.Chrome(executable_path='C:\\Program Files\\chromedriver\\chromedriver.exe')

# American Airlines
american = 'https://www.aa.com/homePage.do'
browser.get(american)

one_way = 'watOneWay'
browser.find_element_by_id(one_way).click() # Selects One Way option

src = 'JFK'
src_id = 'reservationFlightSearchForm.originAirport'
src_elem = browser.find_element_by_id(src_id)
src_elem.clear()
src_elem.send_keys(src)


dest = 'LAX'
dest_id = 'reservationFlightSearchForm.destinationAirport'
dest_elem = browser.find_element_by_id(dest_id)
dest_elem.clear()
dest_elem.send_keys(dest)

dep = '05/15/2019'
dep_id = 'aa-leavingOn'
dep_elem = browser.find_element_by_id(dep_id)
dep_elem.clear()
dep_elem.send_keys(dep)

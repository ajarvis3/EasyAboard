from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path='C:\\Program Files\\chromedriver\\chromedriver.exe')

# Finds an element by its id.
# Sets the element to the given value. Must be a text field.
def set_elem_to_value(id, value):
    elem = browser.find_element_by_id(id)
    elem.clear()
    elem.click()
    elem.send_keys(value)
    elem.send_keys(Keys.ENTER)

def find_and_click(id):
    browser.find_element_by_id(id).click()

# Expedia?
expedia = 'https://www.expedia.com/'
browser.get(expedia)

flights_id = 'tab-flight-tab-hp'
find_and_click(flights_id)

one_way_id = 'flight-type-one-way-label-hp-flight'
find_and_click(one_way_id)

src = 'JFK'
src_id = 'flight-origin-hp-flight'
set_elem_to_value(src_id, src)

dest = 'LAX'
dest_id = 'flight-destination-hp-flight'
set_elem_to_value(dest_id, dest)

depart = '05/25/2019'
depart_id = 'flight-departing-single-hp-flight'
set_elem_to_value(depart_id, depart)

# American Airlines
# american = 'https://www.aa.com/booking/find-flights'
# browser.get(american)

# one_way = 'tabOneWay'
# browser.find_element_by_id(one_way).click() # Selects One Way option

# src = 'JFK'
# src_id = 'segments0.origin'
# src_elem = browser.find_element_by_id(src_id)
# src_elem.clear()
# src_elem.send_keys(src)


# dest = 'LAX'
# dest_id = 'segments0.destination'
# dest_elem = browser.find_element_by_id(dest_id)
# dest_elem.clear()
# dest_elem.send_keys(dest)

# dep = '05/15/2019'
# dep_id = 'segments0.travelDate'
# dep_elem = browser.find_element_by_id(dep_id)
# dep_elem.clear()
# dep_elem.send_keys(dep)

# time = '120001' # All day value
# time_id = 'segments0.travelTime'
# time_elem = Select(browser.find_element_by_id(time_id))
# time_elem.select_by_value(time)

# submit_id = 'flightSearchSubmitBtn'
# submit_elem = browser.find_element_by_id(submit_id)
# submit_elem.click()

#Southwest
# southwest = 'https://www.southwest.com/air/booking/'
# browser.get(southwest)

# trip_type_value = 'oneway'
# trip_type_name = 'tripType'
# trip_type_elem = browser.find_element_by_name(trip_type_name)
# trip_type_elem.click()

# src = 'EWR'
# src_id = 'originationAirportCode'
# set_elem_to_value(src_id, src)


# dest = 'FLL'
# dest_id = 'destinationAirportCode'
# set_elem_to_value(dest_id, dest)


# dep = '06/17'
# dep_id = 'departureDate'
# set_elem_to_value(dep_id, dep)



from pages.flights import Flights

def test_flights(driver):
    flight = Flights(driver)
    flight.load()
    flight.book_flight("Madurai", "Chennai")
    

from pages.flightpayment import FlightPayment

def test_flights(driver):
    flight = FlightPayment(driver)
    flight.load()
    flight.bookflight()
    assert "passenger-details" in driver.current_url
    
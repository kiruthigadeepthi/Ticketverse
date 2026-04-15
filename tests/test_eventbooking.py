from pages.eventbooking import EventBooking

def test_event(driver):
    movie = EventBooking(driver)
    movie.load()
    movie.bookevent()
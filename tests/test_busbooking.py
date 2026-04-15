from pages.busbooking import BusBooking

def test_bus(driver):
    bus = BusBooking(driver)
    bus.load()
    bus.book_bus()
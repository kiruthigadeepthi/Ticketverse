from pages.hotelbooking import Hotelbooking

def test_hotels(driver):
    hotel = Hotelbooking(driver)
    hotel.load()
    hotel.bookhotel()
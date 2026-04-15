from pages.sportsbooking import Sportsbooking

def test_sports(driver):
    sport = Sportsbooking(driver)
    sport.load()
    sport.booksport()
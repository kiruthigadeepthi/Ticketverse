from pages.activitybooking import Activitybooking

def test_activities(driver):
    act = Activitybooking(driver)
    act.load()
    act.bookactivity()
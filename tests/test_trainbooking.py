from pages.trainbooking import TrainBooking

def test_train(driver):
    train = TrainBooking(driver)
    train.load()
    train.book_train()

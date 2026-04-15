from pages.moviebooking import MovieBooking

def test_movie(driver):
    movie = MovieBooking(driver)
    movie.load()
    movie.book_movie()
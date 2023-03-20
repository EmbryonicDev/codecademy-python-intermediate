import unittest
import entertainment

# Write your code below:


class EntertainmentSystemTests(unittest.TestCase):

    def test_movie_license(self):
        daily_movie = entertainment.get_daily_movie()
        licensed_movies = entertainment.get_licensed_movies()

    def test_wifi_status(self):
        wifi_enabled = entertainment.get_wifi_status()


unittest.main()

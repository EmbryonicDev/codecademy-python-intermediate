import unittest
import entertainment


class EntertainmentSystemTests(unittest.TestCase):

    def test_movie_license(self):
        daily_movie = entertainment.get_daily_movie()
        licensed_movies = entertainment.get_licensed_movies()

        # Write your code below:

        self.assertIn(daily_movie, licensed_movies)


unittest.main()

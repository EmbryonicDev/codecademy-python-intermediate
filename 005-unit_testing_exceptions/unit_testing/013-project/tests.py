import unittest
import surfshop


class ShoppingCartTests(unittest.TestCase):
    def setUp(self):
        self.cart = surfshop.ShoppingCart()

    def test_add_surfboards_for_multiple_inputs(self):
        for num in [2, 3, 4]:
            suffix = '' if num == 1 else 's'
            text = f"Successfully added {num} surfboard{suffix} to cart!"
            with self.subTest(num):
                self.assertEqual(self.cart.add_surfboards(num),
                                 f"Successfully added {num} surfboard{suffix} to cart!")
            self.setUp()

    @unittest.skip('Skipping too many boards error')
    def test_too_many_boards_error(self):
        self.assertRaises(surfshop.TooManyBoardsError,
                          self.cart.add_surfboards, 5)

    # @unittest.expectedFailure
    def test_locals_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)


unittest.main()

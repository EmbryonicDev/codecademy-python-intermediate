import unittest
import surfshop
from datetime import datetime, timedelta


class ShoppingCartTests(unittest.TestCase):
    def setUp(self):
        self.cart = surfshop.ShoppingCart()
        self.today = datetime.now()
        print('New cart created')

    def test_add_surfboards_for_multiple_inputs(self):
        for num in [2, 3, 4]:
            suffix = '' if num == 1 else 's'
            text = f"Successfully added {num} surfboard{suffix} to cart!"
            with self.subTest(num):
                self.assertEqual(self.cart.add_surfboards(num),
                                 text)
            self.setUp()
            print('Tested adding surfboards with qty:', num)

    @unittest.skip('Skipping too many boards error')
    def test_too_many_boards_error(self):
        self.assertRaises(surfshop.TooManyBoardsError,
                          self.cart.add_surfboards, 5)
        print('Tested too many boards error')

    # @unittest.expectedFailure
    def test_locals_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)
        print('Tested local discount')

    def test_past_checkout_date(self):
        past_date = self.today - timedelta(days=3)
        self.assertRaises(surfshop.CheckoutDateError,
                          self.cart.set_checkout_date, past_date)
        print('Tested past checkout date')

    def test_future_checkout_date(self):
        future_date = self.today + timedelta(days=3)
        self.cart.set_checkout_date(future_date)
        self.assertEqual(future_date, self.cart.checkout_date)
        print('Tested future checkout date')


unittest.main()

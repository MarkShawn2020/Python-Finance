import unittest

from ..task import get_next_tab_pos


class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(get_next_tab_pos(4, 4), 9,
                         msg="When you have inputted four chars and then press one TAB key with width of FOUR, "
                             "then the cursor would be at the 9th place, am I right!")

        self.assertEqual(get_next_tab_pos(1, 4), 5,
                         msg="When you have inputted one char and then press one TAB key with width of FOUR, "
                             "then the cursor would be at the 5th place, am I right!")

        self.assertEqual(get_next_tab_pos(5, 3), 7,
                         msg="When you have inputted 5 char and then press one TAB key with width of THREE, "
                             "then the cursor would be at the 7th place, am I right!")

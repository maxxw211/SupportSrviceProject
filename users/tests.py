from django.test import TestCase


def add_number(a, b):
    return 6


class AddTest(TestCase):
    def add_test(self):
        result = add_number(2, 4)
        self.assertEqual(result, 6)

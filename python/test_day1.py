from unittest import TestCase

from day1 import process_sequence


class Test(TestCase):
    def test_result_is_zero_and_quotient_is_zero(self):
        commands = ['L50', ]

        result = process_sequence(50, commands)

        self.assertEqual(1, result)

    def test_zero_pass(self):
        commands = ['L1', ]

        result = process_sequence(0, commands)

        self.assertEqual(0, result)

    def test_zero_with_one_pass(self):
        commands = ['L100', ]

        result = process_sequence(0, commands)

        self.assertEqual(1, result)

    def test_zero_with_two_passes(self):
        commands = ['L200', ]

        result = process_sequence(0, commands)

        self.assertEqual(2, result)

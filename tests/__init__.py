#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from nombrestolletres import number_to_letters


class TestToWord(unittest.TestCase):

    def test_to_word(self):
        numbers = [
            1,
            100,
            110,
            101,
            2000,
            102000,
            300000,
            4000000,
            500000000,
            999999998,
            84,
            826.02,
            203.01,
            21.1,
            0.24,
            0.00,
            -230.500,
            '2959163',
            '1000000',
            '150000',
        ]

        results = [
            'un',
            'cent',
            'cent deu',
            'cent un',
            'dos mil',
            'cent dos mil',
            'tres-cents mil',
            'quatre milions',
            'cinc-cents milions',
            'nou-cents noranta-nou milions nou-cents noranta-nou mil nou-cents noranta-vuit',
            'vuitanta-quatre',
            'vuit-cents vint-i-sis amb dos',
            'dos-cents tres amb un',
            'vint-i-un amb deu',
            'zero amb vint-i-quatre',
            'zero',
            'menys dos-cents trenta amb cinquanta',
            'dos milions nou-cents cinquanta-nou mil cent seixanta-tres',
            'un milió',
            'cent cinquanta mil',
        ]

        for result, number in zip(results, numbers):
            self.assertEqual(number_to_letters(number), result)


# -*- coding: utf-8 -*-

import unittest
import random
from gradescope_utils.autograder_utils.decorators import leaderboard


class TestLeaderboard(unittest.TestCase):
    def setUp(self):
        pass

    @leaderboard("high score")
    def test_leaderboard(self, set_leaderboard_value=None):
        """Sets a leaderboard value"""
        set_leaderboard_value(random.randint(0, 10))

    @leaderboard("accuracy")
    def test_leaderboard_float(self, set_leaderboard_value=None):
        """Sets a leaderboard value"""
        set_leaderboard_value(round(random.uniform(50, 100), 2))

    @leaderboard("stars")
    def test_string(self, set_leaderboard_value=None):
        """Sets a leaderboard value"""
        set_leaderboard_value("🌟" * random.randint(0, 10))

    @leaderboard("time", "asc")
    def test_another(self, set_leaderboard_value=None):
        """Sets a leaderboard value that's sorted ascending (lower is better)"""
        set_leaderboard_value(round(random.gauss(7, 3), 2))

import unittest
from random import randint
from gradescope_utils.autograder_utils.decorators import leaderboard


class TestLeaderboard(unittest.TestCase):
    def setUp(self):
        pass

    @leaderboard("high_score")
    def test_leaderboard(self, set_leaderboard_value=None):
        """Sets a leaderboard value"""
        set_leaderboard_value(randint(0, 10))

    @leaderboard("stars")
    def test_string(self, set_leaderboard_value=None):
        """Sets a leaderboard value"""
        set_leaderboard_value("*" * randint(0, 10))

    @leaderboard("time", "asc")
    def test_another(self, set_leaderboard_value=None):
        """Sets a leaderboard value that's sorted ascending (lower is better)"""
        set_leaderboard_value(randint(0, 10))

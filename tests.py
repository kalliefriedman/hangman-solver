import unittest
import requests
from server.py import make_guess, start_game


# class TestHangmanSolverAPIs(unittest.TestCase):
#     """Tests for Hangman Solver project."""

#     def testMakeGuessAPI(self):
#         result = make_guess("1d140bb4ea15", "R")
#         self.assertIn(result, result.get("msg"))

#     def testStartGameAPI(self):
#         result = start_game("julie@yahoo.com")
#         self.assertIn(result, result.get("guessesLeft"))


# class TestFunctionality(unittest.TestCase):
#     def test(self):
#         self.assertEqual(fun(3), 4)

if __name__ == '__main__':
    unittest.main()

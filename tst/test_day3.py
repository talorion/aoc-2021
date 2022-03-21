import unittest
from src.day3 import PuzzleDay3


class TestDay1(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestDay1, self).__init__(*args, **kwargs)
        self.filename: str = "data/test_day3.input"
        self.exp_data: list = [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ]
        self.exp_gamma_rate: int = 22
        self.exp_epsilon_rate: int = 9
        self.exp_power_consumption: int = 198
        self.exp_o2_gen_rating: int = 23
        self.exp_co2_scrub_rating: int = 10
        self.exp_life_support_rating: int = 230

    def test_read_input_file_returns_report(self):
        puzzle = PuzzleDay3()
        report = puzzle.read_input_file(self.filename)
        self.assertEqual(report, self.exp_data)

    def test_find_gamma_rate(self):
        puzzle = PuzzleDay3()
        report = puzzle.read_input_file(self.filename)
        gamma_rate = puzzle.find_gamma_rate(report)
        self.assertEqual(gamma_rate, self.exp_gamma_rate)

    def test_find_epsilon_rate(self):
        puzzle = PuzzleDay3()
        report = puzzle.read_input_file(self.filename)
        epsilon_rate = puzzle.find_epsilon_rate(report)
        self.assertEqual(epsilon_rate, self.exp_epsilon_rate)

    def test_calculate_power_consumption(self):
        puzzle = PuzzleDay3()
        report = puzzle.read_input_file(self.filename)
        power_consumption = puzzle.calculate_power_consumption(report)
        self.assertEqual(power_consumption, self.exp_power_consumption)

    def test_find_o2_gen_rating(self):
        puzzle = PuzzleDay3()
        report = puzzle.read_input_file(self.filename)
        o2_gen_rating = puzzle.find_o2_gen_rating(report)
        self.assertEqual(o2_gen_rating, self.exp_o2_gen_rating)

    def test_find_co2_scrub_rating(self):
        puzzle = PuzzleDay3()
        report = puzzle.read_input_file(self.filename)
        co2_scrub_rating = puzzle.find_co2_scrub_rating(report)
        self.assertEqual(co2_scrub_rating, self.exp_co2_scrub_rating)

    def test_calculate_life_support_rating(self):
        puzzle = PuzzleDay3()
        report = puzzle.read_input_file(self.filename)
        life_support_rating = puzzle.calculate_life_support_rating(report)
        self.assertEqual(life_support_rating, self.exp_life_support_rating)


if __name__ == "__main__":
    unittest.main()

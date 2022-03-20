import unittest
from src.day2 import PuzzleDay2


class TestDay1(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestDay1, self).__init__(*args, **kwargs)
        self.__sample_file: str = 'data/test_day2.input'
        self.__sample_commands: list = [
                                    ('forward', 5),
                                    ('down', 5),
                                    ('forward', 8),
                                    ('up', 3),
                                    ('down', 8),
                                    ('forward', 2)
                                   ]
        self.__expected_coordinates: dict = {
                                        'horizontal_position': 15,
                                        'depth': 10
                                        }
        self.__expected_result: int = 150
        self.__expected_coordinates_with_aim: dict = {
                                        'horizontal_position': 15,
                                        'depth': 60
                                        }
        self.__expected_result_with_aim: int = 900

    def test_read_input_file_returns_report(self):
        puzzle = PuzzleDay2()
        commands: list = puzzle.read_input_file(self.__sample_file)
        self.assertEqual(commands, self.__sample_commands)

    def test_move(self):
        puzzle = PuzzleDay2()
        commands: list = puzzle.read_input_file(self.__sample_file)
        coordinates: dict = puzzle.move(commands)
        self.assertEqual(coordinates, self.__expected_coordinates)

    def test_result(self):
        puzzle = PuzzleDay2()
        commands: list = puzzle.read_input_file(self.__sample_file)
        coordinates: dict = puzzle.move(commands)
        result: int = puzzle.calculate_result(coordinates)
        self.assertEqual(result, self.__expected_result)

    def test_move_with_aim(self):
        puzzle = PuzzleDay2()
        commands: list = puzzle.read_input_file(self.__sample_file)
        coordinates: dict = puzzle.move_with_aim(commands)
        self.assertEqual(coordinates, self.__expected_coordinates_with_aim)

    def test_result_with_aim(self):
        puzzle = PuzzleDay2()
        commands: list = puzzle.read_input_file(self.__sample_file)
        coordinates: dict = puzzle.move_with_aim(commands)
        result: int = puzzle.calculate_result(coordinates)
        self.assertEqual(result, self.__expected_result_with_aim)


if __name__ == '__main__':
    unittest.main()

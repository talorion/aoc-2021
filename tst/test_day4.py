import copy
import unittest
from src.day4 import Board
from src.day4 import PuzzleDay4


class TestDay4(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.filename = "data/test_day4.input"
        self.exp_random_order: list[int] = [
            7,
            4,
            9,
            5,
            11,
            17,
            23,
            2,
            0,
            14,
            21,
            24,
            10,
            16,
            13,
            6,
            15,
            25,
            12,
            22,
            18,
            20,
            8,
            19,
            3,
            26,
            1,
        ]
        self.exp_boards = []
        self.exp_boards.append(
            copy.copy(
                Board(
                    5,
                    [
                        22,
                        13,
                        17,
                        11,
                        0,
                        8,
                        2,
                        23,
                        4,
                        24,
                        21,
                        9,
                        14,
                        16,
                        7,
                        6,
                        10,
                        3,
                        18,
                        5,
                        1,
                        12,
                        20,
                        15,
                        19,
                    ],
                )
            )
        )
        self.exp_boards.append(
            copy.copy(
                Board(
                    5,
                    [
                        3,
                        15,
                        0,
                        2,
                        22,
                        9,
                        18,
                        13,
                        17,
                        5,
                        19,
                        8,
                        7,
                        25,
                        23,
                        20,
                        11,
                        10,
                        24,
                        4,
                        14,
                        21,
                        16,
                        12,
                        6,
                    ],
                )
            )
        )
        self.exp_boards.append(
            copy.copy(
                Board(
                    5,
                    [
                        14,
                        21,
                        17,
                        24,
                        4,
                        10,
                        16,
                        15,
                        9,
                        19,
                        18,
                        8,
                        23,
                        26,
                        20,
                        22,
                        11,
                        13,
                        6,
                        5,
                        2,
                        0,
                        12,
                        3,
                        7,
                    ],
                )
            )
        )
        self.test_rounds: int = 5
        self.exp_turn: int = 12
        self.exp_winner_index: int = 2
        self.exp_winner_score: int = 4512
        self.exp_looser_index: int = 1
        self.exp_looser_score: int = 1924

    def test_read_input_file_returns_report(self):
        puzzle = PuzzleDay4(self.filename)
        boards = puzzle.read_input_file()
        self.assertListEqual(boards, self.exp_boards)

    def test_read_input_file_reads_random_order(self):
        puzzle = PuzzleDay4(self.filename)
        puzzle.read_input_file()
        self.assertSequenceEqual(puzzle.random_order, self.exp_random_order)

    def test_no_win_after_read(self):
        puzzle = PuzzleDay4(self.filename)
        puzzle.read_input_file()
        self.assertIsNone(puzzle.looser())

    def test_no_win_after_5_rounds(self):
        puzzle = PuzzleDay4(self.filename)
        puzzle.read_input_file()
        while puzzle.current_turn < self.test_rounds:
            puzzle.update()
        self.assertIsNone(puzzle.looser())

    def test_winner_after_12_rounds(self):
        puzzle = PuzzleDay4(self.filename)
        puzzle.read_input_file()
        while not puzzle.looser():
            puzzle.update()
        self.assertEqual(puzzle.winning_turn, self.exp_turn)

    def test_winner_is_third_board(self):
        puzzle = PuzzleDay4(self.filename)
        puzzle.read_input_file()
        while not puzzle.looser():
            puzzle.update()
        self.assertEqual(puzzle.winner_index, self.exp_winner_index)

    def test_winner_has_expected_score(self):
        puzzle = PuzzleDay4(self.filename)
        puzzle.read_input_file()
        while not puzzle.looser():
            puzzle.update()
        self.assertEqual(puzzle.winner_score(), self.exp_winner_score)

    def test_looser_is_second_board(self):
        puzzle = PuzzleDay4(self.filename)
        puzzle.read_input_file()
        while not puzzle.looser():
            puzzle.update()
        self.assertEqual(puzzle.looser_index, self.exp_looser_index)

    def test_looser_has_expected_score(self):
        puzzle = PuzzleDay4(self.filename)
        puzzle.read_input_file()
        while not puzzle.looser():
            puzzle.update()
        self.assertEqual(puzzle.looser_score(), self.exp_looser_score)


if __name__ == "__main__":
    unittest.main()

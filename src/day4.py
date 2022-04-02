import copy
import math


class Board:
    def __init__(self, size: int = 0, data: list[int] = []):
        self.size: int = size
        self.data: list[int] = data
        self.draw_numbers: list[int] = []

    def __copy__(self):
        obj = type(self).__new__(self.__class__)
        obj.size = self.size
        obj.data = self.data.copy()
        obj.draw_numbers: list[int] = []
        return obj

    def __str__(self) -> str:
        return f"{self.size} {self. data}"

    def __eq__(self, other) -> bool:
        if self.size != other.size:
            return False
        if self.data != other.data:
            return False
        return True

    def clear(self) -> None:
        self.size = 0
        self.data.clear()

    def add_data(self, raw_data: str) -> None:
        strings = raw_data.strip().split()
        self.data += [int(i.strip()) for i in strings]

    def score(self) -> int:
        score = 0
        for candidate in self.data:
            if candidate in self.draw_numbers:
                continue
            score += candidate
        return score

    def is_winner(self) -> bool:
        marked_rows: list[int] = [0] * self.size
        marked_colums: list[int] = [0] * self.size
        for idx, candidate in enumerate(self.data):
            if candidate in self.draw_numbers:
                marked_rows[math.floor(idx / self.size)] += 1
                marked_colums[idx % self.size] += 1
            if self.size in marked_rows:
                return True
            if self.size in marked_colums:
                return True
        return False

    def update(self, draw: int) -> None:
        if self.is_winner():
            return
        self.draw_numbers += [draw]


class PuzzleDay4:
    def __init__(self, filename: str):
        self.filename: str = filename
        self.random_order: list[int] = []
        self.boards: list[Board] = []
        self.current_turn: int = 0
        self.last_draw: int = None
        self.winner_index: int = None
        self.looser_index: int = None
        self.winner_idexes: list[int] = []
        self.winning_turn: int = None
        self.loosing_turn: int = None

    def __str__(self) -> str:
        return ""

    def read_input_file(self):
        with open(self.filename, "r") as f:
            # fist line is the draw nubers
            strings = f.readline().strip().split(",")
            self.random_order = [int(i.strip()) for i in strings]

            # empty line after draw numbers
            next_line = f.readline()

            idx: int = 0
            board: Board = Board()
            board.clear()
            while True:
                next_line = f.readline()
                stripped_next_line = next_line.strip()
                # EOF
                if not next_line:
                    board.size = idx
                    self.boards.append(copy.copy(board))
                    break
                if not stripped_next_line:
                    board.size = idx
                    self.boards.append(copy.copy(board))
                    board.clear()
                    idx = 0
                    continue
                board.add_data(stripped_next_line)
                idx += 1
        return self.boards

    def winner(self) -> Board:
        if self.winner_index is not None:
            return self.boards[self.winner_index]
        for idx, board in enumerate(self.boards):
            if board.is_winner():
                # self.winning_turn = self.current_turn
                self.winner_index = idx
                self.winner_idexes += [idx]
                return board
        return None

    def looser(self) -> Board:
        self.winner_index = None
        number_of_winners = 0
        max_winners = len(self.boards)
        for idx, board in enumerate(self.boards):
            if board.is_winner() and idx not in self.winner_idexes:
                number_of_winners += 1
                if not self.winning_turn:
                    self.winning_turn = self.current_turn
                self.winner_idexes += [idx]
                self.winner_index = self.winner_idexes[0]
            if len(self.winner_idexes) == max_winners:
                if not self.loosing_turn:
                    self.loosing_turn = self.current_turn
                self.looser_index = self.winner_idexes[max_winners - 1]
                return self.boards[self.looser_index]
        return None

    def update(self) -> None:
        self.current_turn += 1
        if len(self.random_order) < self.current_turn:
            return
        self.last_draw = self.random_order[self.current_turn - 1]
        for board in self.boards:
            board.update(self.last_draw)

    def board_score(self, board: Board, winning_draw: int) -> int:
        if not board:
            return None
        board_score = board.score()
        if not board_score:
            return None
        return board_score * winning_draw

    def winner_score(self) -> int:
        board = self.boards[self.winner_idexes[0]]
        winning_draw = self.random_order[self.winning_turn - 1]
        return self.board_score(board, winning_draw)

    def looser_score(self) -> int:
        board = self.boards[self.winner_idexes[-1]]
        loosing_draw = self.random_order[self.loosing_turn - 1]
        return self.board_score(board, loosing_draw)


if __name__ == "__main__":
    puzzle = PuzzleDay4("data/day4.input")
    puzzle.read_input_file()
    while not puzzle.looser():
        puzzle.update()
    print(f"winning score = {puzzle.winner_score()}")
    print(f"loosing score = {puzzle.looser_score()}")

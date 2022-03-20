class PuzzleDay2:
    def __init__(self, *args, **kwargs):
        self.FORWARD: str = "forward"
        self.DOWN: str = "down"
        self.UP: str = "up"
        self.H_POS: str = "h_pos"
        self.DEPTH: str = "depth"
        self.commands: list = []
        self.coords: dict = {self.H_POS: 0, self.DEPTH: 0}

    def __str__(self) -> str:
        return f"{coords[self.H_POS] * coords[self.DEPTH]}"

    def read_input_file(self, filename: str) -> list:
        f = open(filename, "r")
        for el in f.readlines():
            lst_el = el.strip().split(" ")
            tup_el = tuple([lst_el[0], int(lst_el[1])])
            self.commands.append(tup_el)
        f.close()
        return self.commands

    def move(self, commands: list) -> dict:
        for command in commands:
            if command[0] == self.FORWARD:
                self.coords[self.H_POS] += command[1]
            elif command[0] == self.DOWN:
                self.coords[self.DEPTH] += command[1]
            elif command[0] == self.UP:
                self.coords[self.DEPTH] -= command[1]
        return self.coords

    def move_with_aim(self, commands: list) -> dict:
        aim: int = 0
        for command in commands:
            if command[0] == self.FORWARD:
                self.coords[self.H_POS] += command[1]
                self.coords[self.DEPTH] += command[1] * aim
            elif command[0] == self.DOWN:
                aim += command[1]
            elif command[0] == self.UP:
                aim -= command[1]
        return self.coords

    def calculate_result(self, coords: dict) -> int:
        return coords[self.H_POS] * coords[self.DEPTH]


if __name__ == "__main__":
    puzzle = PuzzleDay2()
    commands: list = puzzle.read_input_file("data/day2.input")
    coords: dict = puzzle.move_with_aim(commands)
    result: int = puzzle.calculate_result(coords)
    print(puzzle)

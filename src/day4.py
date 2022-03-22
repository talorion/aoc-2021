class PuzzleDay4:
    def __init__(self, filename: str):
        self.filename: str = filename
        self.drw_num: str = ""

    def __str__(self) -> str:
        return ""

    def read_input_file(self):
        with open(self.filename, "r") as f:
            self.drw_num = f.readline()
            while True:
                next_line = f.readline()
                if not next_line:
                    break
                self.report.append(next_line.strip())
        return self.report


if __name__ == "__main__":
    pass

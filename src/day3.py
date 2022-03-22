class PuzzleDay3:
    def __init__(self):
        self.filename: str = ""
        self.report: list = []
        self.gamma_rate: int = 0
        self.epsilon_rate: int = 0
        self.power_consumption: int = 0
        self.o2_gen_rating: int = 0
        self.co2_scrub_rating: int = 0
        self.life_support_rating: int = 0
        self.mcb = ""
        self.lcb = ""

    def __str__(self) -> str:
        return f"{self.power_consumption}"

    def read_input_file(self, filename: str) -> list:
        self.filename = filename
        with open(filename, "r") as f:
            while True:
                next_line = f.readline()
                if not next_line:
                    break
                self.report.append(next_line.strip())
        return self.report

    def most_common_bits(self, report: list) -> str:
        self.mcb = ""
        report_sz: int = len(report)
        pos_cnt: list = [0] * len(report[0])
        for idx, num in enumerate(report):
            for idx, dig in enumerate(num):
                pos_cnt[idx] += int(dig)

        for idx, dig in enumerate(pos_cnt):
            if dig >= (report_sz / 2):
                self.mcb += "1"
            else:
                self.mcb += "0"
        return self.mcb

    def least_common_bits(self, report: list) -> str:
        self.lcb = ""
        report_sz: int = len(report)
        pos_cnt: list = [0] * len(report[0])
        for idx, num in enumerate(report):
            for idx, dig in enumerate(num):
                pos_cnt[idx] += int(dig)

        for idx, dig in enumerate(pos_cnt):
            if dig >= (report_sz / 2):
                self.lcb += "0"
            else:
                self.lcb += "1"
        return self.lcb

    def find_gamma_rate(self, report: list) -> int:
        self.most_common_bits(report)
        self.gamma_rate = int(self.mcb, 2)
        return self.gamma_rate

    def find_epsilon_rate(self, report: list) -> int:
        self.least_common_bits(report)
        self.epsilon_rate = int(self.lcb, 2)
        return self.epsilon_rate

    def calculate_power_consumption(self, report: list) -> int:
        self.find_gamma_rate(report)
        self.find_epsilon_rate(report)
        self.power_consumption = self.gamma_rate * self.epsilon_rate
        return self.power_consumption

    def find_o2_gen_rating(self, report: list) -> int:
        report_c: list = report.copy()
        report_el_sz = len(report[0])
        el_idx: int = 0
        while len(report_c) > 1:
            self.most_common_bits(report_c)
            for idx, num in enumerate(report):
                if num[el_idx] != self.mcb[el_idx]:
                    if num in report_c:
                        report_c.remove(num)
            el_idx += 1
            if el_idx >= report_el_sz:
                break
        self.o2_gen_rating = int(report_c[0], 2)
        return self.o2_gen_rating

    def find_co2_scrub_rating(self, report: list) -> int:
        report_c: list = report.copy()
        report_el_sz = len(report[0])
        el_idx: int = 0
        while len(report_c) > 1:
            self.least_common_bits(report_c)
            for idx, num in enumerate(report):
                if num[el_idx] != self.lcb[el_idx]:
                    if num in report_c:
                        report_c.remove(num)
            el_idx += 1
            if el_idx >= report_el_sz:
                break
        self.co2_scrub_rating = int(report_c[0], 2)
        return self.co2_scrub_rating

    def calculate_life_support_rating(self, report: list) -> int:
        self.find_o2_gen_rating(report)
        self.find_co2_scrub_rating(report)
        self.life_support_rating = self.o2_gen_rating * self.co2_scrub_rating
        return self.life_support_rating


if __name__ == "__main__":
    puzzle = PuzzleDay3()
    report = puzzle.read_input_file("data/day3.input")
    puzzle.calculate_power_consumption(report)
    print(puzzle.power_consumption)  # 1997414
    puzzle.calculate_life_support_rating(report)
    print(puzzle.life_support_rating)  # 1032597

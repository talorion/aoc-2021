import unittest
from src.day1 import read_input_file, quantify_descent, filter_report


class TestDay1(unittest.TestCase):
    __sample_file: str = "data/test_day1.input"
    __sample_report: list = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    __expected_descent: int = 7
    __filtered_sample_report: list = [607, 618, 618, 617, 647, 716, 769, 792]
    __expected_filtered_descent: int = 5

    def __init__(self, *args, **kwargs):
        super(TestDay1, self).__init__(*args, **kwargs)

    def test_read_input_file_returns_report(self):
        read_result: list = read_input_file(self.__sample_file)
        self.assertEqual(read_result, self.__sample_report)

    def test_report_descent_quantify(self):
        report: list = read_input_file(self.__sample_file)
        desc = quantify_descent(report)
        self.assertEqual(desc, self.__expected_descent)

    def test_report_can_be_filtered(self):
        report: list = read_input_file(self.__sample_file)
        filtered_report = filter_report(report)
        self.assertEqual(filtered_report, self.__filtered_sample_report)

    def test_filtered_report_descent_quantify(self):
        report: list = read_input_file(self.__sample_file)
        filtered_report = filter_report(report)
        desc = quantify_descent(filtered_report)
        self.assertEqual(desc, self.__expected_filtered_descent)


if __name__ == "__main__":
    unittest.main()

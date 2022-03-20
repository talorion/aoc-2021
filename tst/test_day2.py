
# import unittest
# from src.day2 import read_input_file
# 
# 
# class TestDay1(unittest.TestCase):
# 
#     def __init__(self, *args, **kwargs):
#         super(TestDay1, self).__init__(*args, **kwargs)
#         self.__sample_file: str = "data/test_day2.input"
#         self.__sample_directions = [
#                                     ("forward", 5),
#                                     ("down", 5),
#                                     ("forward", 8),
#                                     ("up", 3),
#                                     ("down", 8),
#                                     ("forward", 2)
#                                    ]
# 
#     def test_read_input_file_returns_report(self):
#         read_result: list = read_input_file(self.__sample_file)
#         self.assertEqual(read_result, self.__sample_directions)
# 
# 
# if __name__ == '__main__':
#     unittest.main()

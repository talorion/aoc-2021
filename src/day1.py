def read_input_file(filename: str) -> list:
    report: list = []
    with open(filename, "r") as f:
        for el in f.readlines():
            num_el = int(el.strip())
            report.append(num_el)
    return report


def quantify_descent(report: list) -> int:
    # count the number of times a depth measurement increases
    # fromfrom the previous measurement.
    desc = 0
    l_el: int = report[0]
    for el in report:
        desc = desc + int(el > l_el)
        l_el = el
    return desc


def filter_report(report: list) -> list:
    filtered_report: list = []
    sz: int = len(report)
    for idx, it in enumerate(report):
        el = it
        if idx + 1 >= sz:
            break
        el += report[idx + 1]

        if idx + 2 >= sz:
            break
        el += report[idx + 2]

        filtered_report.append(el)
    return filtered_report


if __name__ == "__main__":
    report = read_input_file("data/day1.input")
    filter_report = filter_report(report)
    desc = quantify_descent(filter_report)
    print(f"{desc}")

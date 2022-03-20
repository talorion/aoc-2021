def read_input_file(filename: str) -> list:
    commands: list = []
    f = open(filename, "r")
    for el in f.readlines():
        lst_el = el.strip().split(" ")
        tup_el = tuple([lst_el[0], int(lst_el[1])])
        commands.append(tup_el)
    f.close()
    return commands


def move(commands: list) -> dict:
    coordinates: dict = {"horizontal_position": 0, "depth": 0}
    for command in commands:
        if command[0] == "forward":
            coordinates["horizontal_position"] += command[1]
        elif command[0] == "down":
            coordinates["depth"] += command[1]
        elif command[0] == "up":
            coordinates["depth"] -= command[1]
    return coordinates


def move_with_aim(commands: list) -> dict:
    coordinates: dict = {"horizontal_position": 0, "depth": 0}
    aim: int = 0
    for command in commands:
        if command[0] == "forward":
            coordinates["horizontal_position"] += command[1]
            coordinates["depth"] += command[1] * aim
        elif command[0] == "down":
            aim += command[1]
        elif command[0] == "up":
            aim -= command[1]
    return coordinates


def calculate_result(coordinates: dict) -> int:
    return coordinates["horizontal_position"] * coordinates["depth"]


if __name__ == '__main__':
    commands: list = read_input_file("data/day2.input")
    coordinates: dict = move_with_aim(commands)
    result: int = calculate_result(coordinates)
    print(result)

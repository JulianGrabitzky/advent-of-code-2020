file = open("5.txt", "r")
bording_passes = [x.strip() for x in file.readlines()]


def parse_into_set_id(bording_passes):
    return [
        int(
            line.replace("B", "1")
            .replace("F", "0")
            .replace("R", "1")
            .replace("L", "0"),
            2,
        )
        for line in bording_passes
    ]


def get_my_seat_id(lines):
    missing = set(range(min(lines), max(lines)))
    missing.difference_update(lines)
    return next(iter(missing))


print("Task 1: {}".format(max(parse_into_set_id(bording_passes))))
print("Task 2: {}".format(get_my_seat_id(parse_into_set_id(bording_passes))))
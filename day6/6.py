from functools import reduce


def get_file(file_name):
    with open(file_name) as f:
        lines = f.read().split("\n\n")
    return lines


def task1(input):
    return sum([len(set(line.replace("\n", ""))) for line in input])


def task2(input):
    return sum(
        [len(reduce(lambda x, y: x & y, map(set, line.splitlines()))) for line in input]
    )


def main():
    print("Task 1: {}".format(task1(get_file("6.txt"))))
    print("Task 2: {}".format(task2(get_file("6.txt"))))


if __name__ == "__main__":
    main()
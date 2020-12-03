def count_trees(forest, right, down):
    row = 1
    number_of_trees = 0
    while (row * down) < len(forest):
        if forest[row * down][(row * right) % len(forest[0])] == "#":
            number_of_trees += 1
        row += 1
    return number_of_trees


file = open("3.txt", "r")
forest = [l.strip() for l in file.readlines()]
print("Task 1: {}".format(count_trees(forest, 3, 1)))

slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
c = 1
for slope in slopes:
    c *= count_trees(forest, *slope)
print("Task 2: {}".format(c))
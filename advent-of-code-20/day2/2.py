file = open("2.txt", "r")
c = 0
for line in file:
    a = line.split()
    character = a[1][0]
    password = a[2]
    occ = a[0].split("-")
    if password.count(character) in range(int(occ[0]), int(occ[1]) + 1):
        c += 1
print("1: {}".format(c))

file = open("2.txt", "r")
c2 = 0
for line in file:
    a = line.split()
    character = a[1][0]
    password = a[2]
    occ = a[0].split("-")
    first = password[int(occ[0]) - 1] == character
    second = password[int(occ[1]) - 1] == character
    if first != second:
        c2 += 1
print("2: {}".format(c2))
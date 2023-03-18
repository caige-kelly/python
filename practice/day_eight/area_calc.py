from math import ceil

# 1 paint can = 5 square meters
# given random height and width calculate how many cans of paint will need to be bought
# number of cans = (wall height * wall width) / 5 m square
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5


def print_calc(height=test_h, width=test_w, cover=coverage):
    return ceil((height * width) / cover)

result = print_calc()
print(result)
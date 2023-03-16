# Write program which will mark a spot with an X
# The map is made of 3 rows of blank squares

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

position = input("Where do you want to put the trasure? ")
map = [row1, row2, row3]
map[int(position[1])-1][int(position[0])-1] = "X"

print(f'''
{row1}
{row2}
{row3}
''')



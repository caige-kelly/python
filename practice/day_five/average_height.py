student_heights = [156, 178, 165, 171, 187]

sum_height = 0
len_height = 0

for height in student_heights:
    sum_height += height
    len_height += 1

print(f"the average height is {round(sum_height / len_height)}")
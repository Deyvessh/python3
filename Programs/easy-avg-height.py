

student_height = input("Enter a list of student heights: ").split()

for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n]) # this is how to TypeConvert a list from str to int


sum_height = sum(student_height)
num_of_studs = len(student_height)

print(round(sum_height / num_of_studs))

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)


highest = 0

for number in student_scores:
  if highest < number:
    highest = number

print(f"The highest score in the class is: {highest}")


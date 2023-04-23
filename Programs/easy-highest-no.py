
student_score = input("Input a list of student's scores: ").split()

for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
    
    
print(min(student_score))
print(max(student_score))

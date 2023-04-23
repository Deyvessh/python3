
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights: ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  
print(student_heights)
  
# 156 178 165 171 187

# 🚨 Don't change the code above 👆

#Write your code below this row 👇

count = 0

for heightnumber in student_heights:
    count += 1


temp = 0 
for sum in student_heights:
    
    sum += temp
    temp = sum


avg_height = sum / count
print(round(avg_height))
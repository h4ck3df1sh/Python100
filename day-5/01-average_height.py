# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Example input 
# student_heights = 180 124 165 173 189 169 146

#Write your code below this row 👇

average_student_heights = 0
student_count = 0
for height in student_heights:
    student_count += 1
    average_student_heights += height

average_student_heights = round(average_student_heights / student_count)
print(average_student_heights)
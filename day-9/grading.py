student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for student,score in student_scores.items():
    grade = ""
    if 70 < score <= 80:
        grade = "Acceptable"
    elif 80 < score <= 90:
        grade = "Exceeds Expectations"
    elif 90 < score <= 100:
        grade = "Outstanding"
    else:
        grade = "Fail"
    
    student_grades[student] = grade
# 🚨 Don't change the code below 👇
print(student_grades)
student_grades.up

# Student Marks, Percentage and Grade

name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))

total = 0
marks = []

for i in range(1, n + 1):
    mark = float(input(f"Enter mark for Subject {i}: "))
    marks.append(mark)
    total += mark

percentage = total / n
highest = max(marks)
lowest = min(marks)
passed=0
for mark in marks:
    if mark>=35:
        passed+=1

if percentage >= 90:
    grade, performance = "A+", "Outstanding"
elif percentage >= 80:
    grade, performance = "A", "Excellent"
elif percentage >= 70:
    grade, performance = "B", "Very Good"
elif percentage >= 60:
    grade, performance = "C", "Good"
elif percentage >= 50:
    grade, performance = "D", "Average"
else:
    grade, performance = "F", "Needs Improvement"

print("\n--- Academic Performance Report ---")
print("Student Name :", name)
print("Total Marks  :", total, "/", n * 100)
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)
print("Performance  :", performance)
print("Highest Mark :", highest)
print("Lowest Mark  :", lowest)
print("Subjects Passed :", passed, "/", n)
print("Subjects Failed :", n - passed)
if passed==n:
    print("Result  :","PASS")
else:
    print("Result  :Fail")

if percentage >= 90:
    print("Remark: Excellent achievement! Keep it up!")
elif percentage >= 75:
    print("Remark: Great work! Keep improving!")
else:
    print("Remark: More practice can improve your results.")

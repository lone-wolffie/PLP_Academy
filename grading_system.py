#Ask user to input their score
score = int(input("Enter your score (0-100): "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

#Print the result
print(f"Your grade is: {grade}")


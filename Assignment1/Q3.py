# User input for final scores of 10 courses
num_courses = 10
total_sum = 0.00
for x in range(num_courses):
    score = input('Enter final score for course')
total_sum = total_sum + int(score)
average = total_sum / 10

print('Total:', total_sum)
print('average score:', average)



if float(average) > 90:
    grade = 'A'
elif float(average) > 80:
    grade = 'B'
elif float(average) > 75 and float(average) <= 79:
    grade = 'C'
elif float(average) > 60:
    grade = 'D'
elif float(average) < 59:
    grade = 'F'






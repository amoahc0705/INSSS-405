def calculate_grade(scores):
    total = sum(scores)
    mean = total/ len(scores)

    if mean >= 90:
        grade = 'A'
    elif mean >= 80:
        grade = 'B'
    elif mean >= 70:
        grade = 'C'
    elif mean >= 60:
        grade = 'D'
    elif mean >= 50:
        grade = 'E'
    else:
        grade = 'F'

    return mean, grade

def collect_scores(num_users):
    scores = []
    for i in range(num_users):
        score = float(input(f"Enter the final grade for user {i+1}: "))
        scores.append(score)
    return scores

# Collect scores from users
num_users = 3
scores = collect_scores(num_users)

# Calculate mean and grade
mean, final_grade = calculate_grade(scores)

# Print the results
print(f"Mean: {mean}")
print(f"Final Grade: {final_grade}")


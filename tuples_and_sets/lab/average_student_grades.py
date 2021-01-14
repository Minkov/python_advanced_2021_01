def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines

#
# n = int(input())
# students_grades_lines = input_to_list(n)


students_grades_lines = (
    'Vladimir 4.00',
    'Petko 3.00',
    'Vladimir 5.00',
    'Petko 3.66',
)


def avg(values):
    return sum(values) / len(values)


students_grades = {}

for line in students_grades_lines:
    student, grade = line.split(' ')
    if student not in students_grades:
        students_grades[student] = []
    students_grades[student].append(float(grade))

for (student, grades) in students_grades.items():
    # grades_string = ' '.join(map(lambda grade: f'{grade:.2f}', grades))
    grades_string = ' '.join(f'{grade:.2f}' for grade in grades)
    avg_grade = avg(grades)
    print(f'{student} -> {grades_string} (avg: {avg_grade:.2f})')

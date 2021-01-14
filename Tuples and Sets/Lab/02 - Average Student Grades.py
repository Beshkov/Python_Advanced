repeat = int(input())

students = {}


def avg(value):
    return sum(value) / len(value)


for _ in range(repeat):
    name, mark = input().split(' ')

    if name not in students:
        students[name] = []
    students[name].append(float(mark))

for student, marks in students.items():
    grades_str = ' '.join(map(lambda mark: f'{mark:.2f}',marks))
    print(f"{student} -> {grades_str} (avg: {avg(marks):.2f})")

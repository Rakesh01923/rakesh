class Student:
    def __init__(self, reg, name, m1, m2, m3):
        self.reg = reg
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3

a = int(input("How many data do you want to enter: "))
stud = {}
for i in range(a):
    reg = int(input("Enter Your Reg.No: "))
    name = input("Enter your Name: ")
    mark1 = int(input("Enter mark1: "))
    mark2 = int(input("Enter mark2: "))
    mark3 = int(input("Enter mark3: "))

    st = Student(reg, name, mark1, mark2, mark3)
    stud[reg] = st

avg_marks = [(reg, st.average()) for reg, st in stud.items()]

for i in range(len(avg_marks)):
    for j in range(i + 1, len(avg_marks)):
        if avg_marks[i][1] < avg_marks[j][1]:
            avg_marks[i], avg_marks[j] = avg_marks[j], avg_marks[i]

ranked_students = {}
rank = 1
for reg, avg in avg_marks:
    ranked_students[reg] = {'student': stud[reg], 'average': avg, 'rank': rank}
    rank += 1

for reg, info in ranked_students.items():
    st = info['student']
    print(f"Reg.No: {st.reg}, Name: {st.name}, Average: {info['average']:.2f}, Rank: {info['rank']}")

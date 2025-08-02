class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        if score >= 0 and score <= 100:
            self.scores.append(score)

    def average_score(self):
        if len(self.scores) == 0:
            return 0
        return round(sum(self.scores) / len(self.scores), 2)

    def passed(self):
        return self.average_score >= 60  

students = [
    Student("Alice"),
    Student("Bob"),
    Student("Charlie")
]

students[0].add_score(80)
students[0].add_score(90)

students[1].add_score(50)
students[1].add_score(55)

students[2].add_score(70)

for student in students:
    print(f"{student.name} - Average: {student.average_score()} - Passed: {student.passed()}")

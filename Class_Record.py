from Student import Student
from Grade import Grade

student= Student("Christian Rabadon",22)

grades = [
    Grade("CPE028", 3, 75),
    Grade("CPE025", 4, 82),
    Grade("CPE103", 3, 87),
]

student.record = grades


for grade in student.record:
    print(grade)
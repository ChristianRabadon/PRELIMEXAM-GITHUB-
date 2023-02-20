class Grade:
    def __init__(self, course_code, course_units, course_grade):
        self.course_code = course_code
        self.course_units = course_units
        self.course_grade = course_grade

    def __str__(self):
        return f"Course Code: {self.course_code}, Course Units: {self.course_units}, Course Grade: {self.course_grade}"

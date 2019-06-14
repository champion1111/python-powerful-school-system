"""
action
connet with [student.py] [main.py]
"""

class School:
    def __init__(self):
        print("welcome to the list!")
        self.students = []

    def add_student(self, s):
        self.students.append(s)

    def get_student(self, name):
        for s in self.students:
            print(s.name)
            if s.name == name:
                return s

    def print(self):
        print("=-=-=-=-=-=-= Total =-=-=-=-=-=-=")
        for s in self.students:
            print(f"{s.name} {s.sex} {s.idnumber} {s.score} {s.average()}")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    
    def list_fail(self):
        for s in self.students:
            for sc in s.score:
                if sc < 60:
                    print(f"{s.name} is fail.")

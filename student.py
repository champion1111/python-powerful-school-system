"""
store class
connet with [school.py] [main.py]
"""

class Student:
    def __init__(self, name, sex, idnumber):
        self.name = name
        self.sex = sex
        self.score = []
        self.idnumber = idnumber

    def print(self):
        print(self.name)
        print(self.sex)
        print(self.score)
        print(self.idnumber)

    def add_score(self, s):
        self.score.append(s)

    def average(self):
        total = 0.0
        for s in self.score:
            total += s
        if len(self.score) != 0:
            return total / len(self.score)
        else:
            return None

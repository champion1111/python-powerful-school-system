"""
the main part
connet with [student.py] [school.py]
"""

from school import School
from student import Student

sc = School()

while(True):
    cmd = input("which do you want??\n** Press [ctrl+c] to quit\nadd_Student(ast)\tprint_All(p)\tadd_Score(asc)\tcheck_fail(cf)\nidiot(li)\tgenius(lg)")
    if cmd == "ast":
        name = input("name: ")
        sex = input("sex [M/F]: ")
        idnumber = input("idnumber: ")
        s = Student(name, sex, idnumber)
        while(True):
            score = int(input("Score: (-0 to quit)"))
            if score == -0:
                break
            else:
                s.add_score(score)
        sc.add_student(s)
    elif cmd == "p":
        sc.print()
    elif cmd == "asc":
        name = input("name: ")
        score = int(input("score: "))
        s = sc.get_student(name)
        s.add_score(score)
    elif cmd == "cf":
        sc.list_fail()
    elif cmd == "lg":
        sc.list_genious()
    elif cmd == "li":
        sc.list_idiot()

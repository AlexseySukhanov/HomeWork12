from student import Student
"""
Class describes group of students
"""
class Group:

    def __init__(self, groupname, students):
        self.groupname = groupname
        self.group = students

    def find(self, surn):
        for i in self.group:
            if i.surname == surn:
                return f'Name: {i.name} ID Number: {i.idnumber}'

    def rem(self,id):
        for i in range(len(self.group)):
            if self.group[i].idnumber == id:
                return self.group.pop(i)

    def __str__(self):
        s=""
        for i in self.group:
            s+=str(i.surname)+" "
        return s


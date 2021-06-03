
class Student:
    studentLevel = 'first year computer science 2020/2021 session'
    studentCounter = 0
    registeredCourse='csc102'
    def __init__(self, thename, thematricno, thesex,thehostelname,theage,thecsc102examscore):
        self.name = thename
        self.matricno = thematricno
        self.sex = thesex
        self.hostelname =thehostelname
        self.age=theage
        self.csc102examscore=thecsc102examscore

        Student.studentCounter = Student.studentCounter + 1

    def getName(self):
        return  self.name

    def setName(self, thenewName):
        self.name = thenewName

    def agedeterminer(self):
        if self.age>16:
            print('Student is above 16')

    def finalscore(self):
        if self.csc102examscore < 45:
            print('You will carryover this course, sorry')
        else:
            print('You have passed')


    @classmethod
    def course():
         print(f'Students registered course is {Student.registeredCourse}')

    @staticmethod
    def PAUNanthem():
        print('Pau, here we come, Pau, here we come ')

    @staticmethod
    def ODDorEVEN(num):
        if num % 2==0:
            print('Number is even')
        else:
            print('Number is odd')    

    @classmethod
    def studentnum(cls):
        print(Student.studentCounter)

studendt1 = Student('James Kaka', '021074', 'M','Amethyst','16', '49')
print(studendt1.getName())
studendt1.setName('James Gaga')
print(studendt1.getName())

Student.PAUNanthem()
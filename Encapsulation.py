class Student:
    __schoolName='PAU'
    def __init__(self,thename,thematricno):
        self. __name=thename
        self.__matric=thematricno
    
    def __display(self):
        print('This is a private method')

    def getdisplay(self):
       self.__display()

    def getname(self):
        return self.__name

    def setname(self):
        self.__name='Kaka Brownn'

thestudent=Student('Kaka Brown', '0021072')
thestudent.getdisplay()
print(thestudent.getname())        


class Person:
    def __init__(self,name,family,age,nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality
    
    def Print(self):
        print("I'm {} {} and I'm {}!".format(self.name, self.family, self.nationality))

class Student(Person):
    def __init__(self,name,family,age,nationality,university,year_of_study):
        Person.__init__(self,name,family,age,nationality)
        self.year_of_study = year_of_study
        self.university = university
    
    def Print(self):
        print("I'm {} {} and I'm {}! I'm Student in {} and I started in {} year !".format(self.name, self.family, self.nationality,self.university,self.year_of_study))

class Lecturer(Person):
    def __init__(self,name,family,age,nationality,university,experience):
        Person.__init__(self,name,family,age,nationality)
        self.experience = experience
        self.university = university
    
    def Print(self):
        print("I'm {} {} and I'm {}! I'm Lecturer in {} and I have {} years of experience!".format(self.name, self.family, self.nationality,self.university,self.experience))


Person1=Person("Petur","Nikolv",12,"Bulgarian")
Person2=Person("Niki","Petrov",17,"American")
St1=Student("Niki","Petrov",17,"American","TU",2021)
St2=Student("Petur","Nikolv",12,"Bulgarian","SU",2019)
Lc1=Lecturer("Niki","Petrov",17,"American","TU",5)
Lc2=Lecturer("Petur","Nikolv",12,"Bulgarian","SU",2)

list=[Person1,Person2]
list1=[St1,St2]
list2=[Lc1,Lc2]


for person in list:
    person.Print()

for st in list1:
    st.Print()

for lc in list2:
    lc.Print()
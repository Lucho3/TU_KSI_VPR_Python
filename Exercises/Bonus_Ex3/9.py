class Student:
    def __init__(self,student_id,student_name):
        self.student_id = student_id
        self.student_name = student_name

st1=Student(1,"Petur")
print(st1.student_id)
print(st1.student_name)

st1.student_class="Class1"

print(st1.student_class)
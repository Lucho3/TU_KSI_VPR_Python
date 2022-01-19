from Student import Student
import sys

class Group:
    def __init__(self):
        self.list_of_students=list()
        self.list_of_students_with_A=list()

    def get_students_from_file(self,file_name):
        with open(file_name, 'r') as file:
            for line in file:
                st=[el for el in line.split()]
                student=Student(st[0],st[1],float(st[2]))
                self.list_of_students.append(student)

    def add_student(self,name,fNum,success_rate):
        not_in_list=True
        for student in self.list_of_students:
            if name==student.name and fNum==student.f_num:
                not_in_list=False

        if not_in_list:
            student=Student(name,fNum,int(success_rate))
            self.list_of_students.append(student)

        else:
            print("The student is already in the list!")

    def remove_students_with_bad_grades(self):
        for student in self.list_of_students:
            if student.success_rate<3:
                self.list_of_students.remove(student)

    def average_success_rate(self):
        avg=0
        for student in self.list_of_students:
            avg+=student.success_rate
        print(avg/len(self.list_of_students))

    def max_success_rate(self):
        max = -sys.maxsize - 1
        for student in self.list_of_students:
            if student.success_rate>max:
                max=student.success_rate

        print(max)

    def __max_success_rate(self):
        max = -sys.maxsize - 1
        for student in self.list_of_students:
            if student.success_rate>max:
                max=student.success_rate

        return max

    def min_success_rate(self):
        min = sys.maxsize
        for student in self.list_of_students:
            if student.success_rate < min:
                min = student.success_rate

        print(min)

    def print_group(self):
        for st in self.list_of_students:
            print(st.name,st.f_num,st.success_rate)

    def students_with_a(self):
        for st in self.list_of_students:
            if st.name[0]=='a' or st.name[0]=='A':
                self.list_of_students_with_A.append(st)

    def clear_list(self):
        self.list_of_students.clear()

    def info_for_students_with_similar_success(self,student):
        for st in self.list_of_students:
            if st.success_rate==student.success_rate:
                print(st)

    def even_f_num_max_success(self):
        for st in self.list_of_students:
            last_digit=int(st.f_num[len(st.f_num)-1])
            if st.success_rate==self.__max_success_rate and last_digit%2==0:
                print(st)

    def odd_f_num(self):
        for st in self.list_of_students:
            last_digit=int(st.f_num[len(st.f_num)-1])
            if last_digit%2==1:
                print(st)

    def print_group_with_a(self):
        for st in self.list_of_students_with_A:
            print(st)

    def print_students_in_file(self):
        if len(self.list_of_students)>0:
             f = open("Printed_students.txt", "w")
             for st in self.list_of_students:
                  f.write(str(st))
                  f.write("\n")
             f.close()
        else:
            print("Empty list Exception!")


from Group import Group

gr1=Group()
gr1.get_students_from_file("Group.txt")
gr1.print_group()
gr1.max_success_rate()
gr1.min_success_rate()
gr1.average_success_rate()
gr1.remove_students_with_bad_grades()
gr1.print_group()
gr1.add_student("Petur_Nikolov_Petrov","121221311",5.4)
gr1.add_student("Luboslav_Mitrev_Ivanov","121221333",4.5)
gr1.print_group()
gr1.add_student("Lyboslav_Mitrev_Ivanov","121221333",4.5)
gr1.print_group()
gr1.average_success_rate()

gr1.students_with_a()
print(gr1.list_of_students_with_A)
# gr1.print_group()
# gr1.clear_list()
# print("ok")
print(gr1.info_for_students_with_similar_success(gr1.list_of_students[0]))
gr1.even_f_num_max_success()
gr1.odd_f_num()
gr1.print_group_with_a()

gr1.print_students_in_file()
json1=gr1.list_of_students[0].convert_to_json()
print(json1)
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] # то что дано по заданию
print(grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # дано по заданию
print(students) # в консоли очерёдность имён меняется
students = ('Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron')
n1, n2, n3, n4, n5 = students
print('Так соотносятся имена с оценками по данным, с которыми мы работаем.')
print([n1 + '-' + str(grades[0]), n2 + '-' + str(grades[1]), n3 + '-' + str(grades[2]), n4 + '-' + str(grades[3]), n5 + '-' + str(grades[4])])
J_grade = grades[0]
B_grade = grades[1]
S_grade = grades[2]
K_grade = grades[3]
A_grade = grades[4]
J_average = sum(grades[0]) / len(grades[0])
B_average = sum(grades[1]) / len(grades[1])
S_average = sum(grades[2]) / len(grades[2])
K_average = sum(grades[3]) / len(grades[3])
A_average = sum(grades[4]) / len(grades[4])
students = sorted(tuple(students))
students_grades = {students[0]: A_average, students[1] : B_average, students[2] : J_average, students[3] : K_average, students[4] : S_average}
print('Такой ответ если соотносить имена так, как дано по заданию.')
print(students_grades, '\n')
# у меня итоговвый результат в консоли, !!!различается с тем, что указано в задании, так как у меня оценки учеников
# идут по тому же порядку в котором идут их имена, а взадании
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] # то что дано по заданию
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # дано по заданию
students = sorted(tuple(students))
grades[0] = sum(grades[0]) / len(grades[0])
grades[1] = sum(grades[1]) / len(grades[1])
grades[2] = sum(grades[2]) / len(grades[2])
grades[3] = sum(grades[3]) / len(grades[3])
grades[4] = sum(grades[4]) / len(grades[4])
answer_dict = {students[0] : grades[0], students[1] : grades[1], students[2] : grades[2], students[3] : grades[3], students[4] : grades[4]}
print('Ответ, указаный в задании, получается, если соотносить оценки, в изначальной очёредности, к миенам, которые были выставлены в алфавитном порядке.')
print(answer_dict)
# в этом ответе порядок оценок не меняется и к ним подствляются мена в алфавитном порядке

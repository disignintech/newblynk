def find_average_marks(marks):
    sum_of_marks = sum(marks)
    number_of_subjects = len(marks)
    
    average_marks = sum_of_marks/number_of_subjects
    
    return average_marks

# compute grade and return it
def compute_grade(average_marks):
    if average_marks >= 80.0:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'F'
    
    return grade
subjects0_marks = int(input("enter your subjects_marks : "))
subjects1_marks = int(input("enter your subjects_marks : "))
subjects2_marks = int(input("enter your subjects_marks : "))
subjects3_marks = int(input("enter your subjects_marks : "))
subjects4_marks = int(input("enter your subjects_marks : "))
subjects5_marks = int(input("enter your subjects_marks : "))
marks = [subjects0_marks, subjects1_marks, subjects2_marks, subjects3_marks, subjects4_marks, subjects5_marks]
average_marks = find_average_marks(marks)
grade =compute_grade(average_marks)

print("Your average marks is", average_marks)
print("Your grade is", grade)
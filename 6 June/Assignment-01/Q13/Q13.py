def calculate_average(marks):
    return sum(marks) / len(marks)

student_marks = {
    "Student 1": [0, 0, 5, 2, 8],
    "Student 2": [5, 2, 8, 9, 1],
    "Student 3": [0, 5, 2, 8, 5],
    "Student 4": [8, 2, 6, 0, 8],
    "Student 5": [5, 2, 8, 0, 7]
}


average_marks = {student: calculate_average(marks) for student, marks in student_marks.items()}

max_student = max(average_marks, key=average_marks.get)
max_average = average_marks[max_student]


min_student = min(average_marks, key=average_marks.get)
min_average = average_marks[min_student]

print("Student with maximum average marks:")
print(f"Student: {max_student}")
print(f"Average Marks: {max_average}")

print("\nStudent with minimum average marks:")
print(f"Student: {min_student}")
print(f"Average Marks: {min_average}")

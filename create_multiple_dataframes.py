import pandas as pd
student_data = {
    "Roll_No": [101, 102, 103],
    "Name": ["Harshi", "Prathibha", "Shanvika"],
    "Department": ["IT", "IT", "CSE"],
    "Percentage": [95, 90, 89]
}
course_data = {
    "course_ID": ["C101", "C102", "C103"],
    "course_name": ["python", "data science", "machine learning"],
    "credits": [4, 3, 4]
}
students_df = pd.DataFrame(student_data)
courses_df = pd.DataFrame(course_data)
print("Students DataFrame:")
print(students_df)
print("\nCourses DataFrame:")
print(courses_df)
import pandas as pd
student_data = {
    "Roll_No": [101, 102, 103],
    "Name": ["Harshi", "Prathibha", "Abhi"],
    "Department": ["IT", "IT", "CSE"],
    "Percentage": [95, 90, 92]
}
course_data = {
    "course_ID": ["C101", "C102", "C103"],
    "course_name": ["python", "data science", "machine learning"],
    "credits": [4, 3, 4]
}
students_df = pd.DataFrame(student_data)
courses_df = pd.DataFrame(course_data)
excel_data = {
    "students": students_df,
    "courses": courses_df
}
print("Available_sheets:")
print(excel_data.keys())
print("\nStudent_sheet:")
print(excel_data["students"])
print("\nCourse_sheet:")
print(excel_data["courses"])
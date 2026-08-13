import pandas as pd
from io import StringIO
JSON_string = """
[
    {"Roll_No": 201, "Name": "HARSHI", "Percentage": 91},
    {"Roll_No": 202, "Name": "PRATHIBHA", "Percentage": 90}
]
"""
parsed_json_df = pd.read_json(StringIO(JSON_string))
print("\nParsed JSON string:")
print(parsed_json_df)
student_df = parsed_json_df
student_df.to_excel(
    "students.xlsx",
    sheet_name="student Details",
    index=False
)
print("\nExcel Data (based on the DataFrame saved):")
print(student_df)
print("\nAll file operations completed successfully")
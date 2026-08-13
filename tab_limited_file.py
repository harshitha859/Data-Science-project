import pandas as pd
student_data={
    "Roll_No":[101,102,103,104],
    "Name":["Harshi","Prathibha","Shanvika","Abhi"],
    "Department":["IT","IT","CSE","ECE"],
    "Percentage":[96,95,80,90]
}
student_df = pd.DataFrame(student_data)
student_df.to_csv(
    "student_output.txt",
    sep="\t",
    index=False
)
task_df=pd.read_csv(
    "student_output.txt",
    sep="\t"
)
print("\n Tab_limited Data:")
print(task_df)
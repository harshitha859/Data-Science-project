import pandas as pd
student_data={
    "Roll_No":[101,102,103,104],
    "Name":["Harshi","Prathibha","Shanvika","Abhi"],
    "Department":["IT","IT","CSE","ECE"],
    "Percentage":[90,89,80,79],
}
df=pd.DataFrame(student_data)
print(df)
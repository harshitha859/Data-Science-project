import pandas as pd
from io import StringIO
json_data="""
[
{
  "Roll_No":101,
  "Name":"Harshi",
  "Marks":96
},
{
  "Roll_No":102,
  "Name":"Prathibha",
  "Marks":90
},
{
  "Roll_No":103,
  "Name":"Shanvika",
  "Marks":85
}
]
"""
df=pd.read_json(StringIO(json_data))
print("Parsed json Data")
print(df)
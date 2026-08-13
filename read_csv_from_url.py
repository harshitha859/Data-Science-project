import pandas as pd
from io import StringIO
csv_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
csv_df = pd.read_csv(csv_url)
print("csv Data:")
csv_df.to_csv("iris_output.csv", index=False)
print("\ncsv file written successfully")
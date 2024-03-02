import pandas as pd

df = pd.read_csv(
    "hrdata.csv",
    index_col="Employee",
    parse_dates=["Hired"],
    header=0,
    names=["Employee", "Hired", "Salary", "Sick Days"],
)

# Replace '%Y-%m-%d' with the actual format of your dates (e.g., '%d/%m/%Y')
# df["Hired"] = pd.to_datetime(df["Hired"], format="%y-%mm-%d")

# Writing to a file with pandas
df.to_csv("hrdata_modified.csv")

# print(df)

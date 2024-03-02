import pandas as pd
# import data_raw

# df = pd.DataFrame(data=data_raw.data, index=data_raw.columns).T
# df.to_csv("data.csv")  # Write to csv file

df = pd.read_csv("data.csv", index_col=0)  # Read from csv file
print(df)

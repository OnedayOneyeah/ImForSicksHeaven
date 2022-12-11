import pandas as pd

df = pd.read_csv("../data/merged_final.csv")
# df["date"] = pd.to_datetime(df["date"])




def get_all ():
    return df

import pandas as pd

df = pd.read_csv("../data/merged_final.csv")
# df["date"] = pd.to_datetime(df["date"])

scaled_list = []
scaled_list.append(pd.read_csv("../data/scaled_data/data_scaled_sd.csv"))
scaled_list.append(pd.read_csv("../data/scaled_data/data_scaled_nm.csv"))
scaled_list.append(pd.read_csv("../data/scaled_data/data_scaled_mm.csv"))
scaled_list.append(pd.read_csv("../data/scaled_data/data_scaled_rb.csv"))


def get_all ():
    return df

def get_scaled(number):
    return scaled_list[number]



# filter data which starts with I letter
import pandas as pd

def filter_data():
    print("Applying condition to the countries which starts with I letter")
    df = pd.read_csv("~/ip_files/Life_expect_cleaned.csv")

    df = df[df['Entity'].str.startswith("I").reset_index(drop=True)]
    df.to_csv("~/op_files/countries_filter.csv")

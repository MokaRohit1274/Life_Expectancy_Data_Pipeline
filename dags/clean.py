import pandas as pd
import datetime
from pathlib import Path

def pre_process():
    print("Before adding date column")

    input_path = Path("~/ip_files/Life_expectancy.csv").expanduser()
    output_path = Path("~/ip_files/Life_expect_cleaned.csv").expanduser()

    df = pd.read_csv(input_path)
    df["process_date"] = datetime.date.today()
    df = df.fillna("empty String")
    df.to_csv(output_path, index=False)

    print("File is cleansed and date is added in file")

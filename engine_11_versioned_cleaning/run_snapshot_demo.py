import pandas as pd
from src.data_snapshot import create_data_snapshot
from src.version_tracker import register_new_version
from src.diff_engine import generate_diff_report

df1 = pd.read_csv("data/raw_v1.csv")
v1 = register_new_version(create_data_snapshot(df1, "raw_v1.csv"))

df2 = pd.read_csv("data/raw_v2.csv")
v2 = register_new_version(create_data_snapshot(df2, "raw_v2.csv"))

diff = generate_diff_report(v1, v2)
print(diff)

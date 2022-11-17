import sys
import glob
import pandas as pd
folder_path=sys.argv[1]
choice=sys.argv[2]
csv_files=glob.glob(folder_path+"/*.CSV")
df=(pd.read_csv(file) for file in csv_files)
combined=pd.concat(df)
print(df)
print(combined)
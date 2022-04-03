import os
import pandas as pd
from datetime import datetime

df_list = []

for filename in os.listdir():
    if 'scouting_record' in filename and filename.endswith('.csv'):
        df_list.append(pd.read_csv(filename))

df = pd.concat(df_list)

now_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')

df = df.sort_values(by='time')

out_file = f'compiled_scouting_data{now_time}.csv'
df.to_csv(out_file, index=False)

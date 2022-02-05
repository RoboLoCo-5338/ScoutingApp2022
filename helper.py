import pandas as pd
import os

'''
df = pd.DataFrame({
    'Team_Name': [],
    'Boxes_Carried': [],
    'Boxes_Controlled': [],
    'Accidents': []
})

df.to_csv('./observations/BunnyBots.csv')
'''

df = pd.read_csv('./observations/BunnyBots.csv')

data = {
    'team_name': pd.Series(['awepfiowejf']),
    'boxes_carried': pd.Series(['apowiefjaef']),
    'boxes_controlled': pd.Series(['apeoiwejfo']),
    'accidents': pd.Series(['awpeofijef'])
}

df = df.append(pd.DataFrame(data), ignore_index=True)

'''
df['team_name'] = df['team_name'].append(df['team_name'], ignore_index=True)
df['boxes_carried'] = df['boxes_carried'].append(df['boxes_carried'], ignore_index=True)
df['boxes_controlled'] = df['boxes_controlled'].append(df['boxes_controlled'], ignore_index=True)
df['accidents'] = df['accidents'].append(df['accidents'], ignore_index=True)
'''

print(df)

df.to_csv('./observations/BunnyBots.csv', index=False) 
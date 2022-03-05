from flask import Flask, render_template, request, url_for, redirect
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import json
from multiprocessing import Value
import time
import pandas as pd
import math
import numpy as np

balls_shot = Value('i', 0)
accidents = Value('i', 0)
e1 = Value('i', 0)
e2 = Value('i', 0)

app = Flask(__name__)

def init_sheet(sheet_num):
    scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

    client = gspread.authorize(creds)

    if sheet_num == 1:
        sheet = client.open("RoboLoco-Scouting-Test").worksheet('teleop')
    if sheet_num == 2:
        sheet = client.open("RoboLoco-Scouting-Test").worksheet('autonomous')

    return sheet

@app.route('/', methods=['GET', 'POST'])
def home():
    balls_shot = 0
    if request.method == 'POST':
        for key, val in request.form.items():
            if key == 'team_name':
                context = {
                    'team_name': val
                }

                with open('./team_name.txt', 'w') as f:
                    f.write(val)

        return redirect('/observing')
    if request.method == 'GET':
        return render_template('home.html')

def analytics_display(mode):
    if mode == 'teleop':
        sheet = init_sheet(1)
    else:
        sheet = init_sheet(2)

    data = sheet.get_all_records()

    graph_data = {}
    radar_data = {}
    high_goals = {}
    low_goals = {}
    climb_hash = {}
    name_set = set([])

    for record in data:
        team_name = record['team_name'] 
        if team_name not in name_set:
            name_set.add(team_name)
            graph_data.update({team_name: []})
            radar_data.update({team_name: []})
            high_goals.update({team_name: []})
            low_goals.update({team_name: []})
            climb_hash.update({team_name: []})

        high_goal = int(record['high_goal'])
        low_goal = int(record['low_goal'])
        climb = int(record['climb'])

        total_score = (2*high_goal) + low_goal + climb

        graph_data[team_name].append(total_score)
        high_goals[team_name].append(high_goal)
        low_goals[team_name].append(low_goal)
        climb_hash[team_name].append(climb)

        if len(radar_data[team_name]) > 0:
            radar_data[team_name][0][0] += high_goal
            radar_data[team_name][0][1] += low_goal 
            radar_data[team_name][0][2] += climb

        else:
            radar_data[team_name].append([high_goal, low_goal, climb])
    
    listify = lambda l: [[str(key), l[key]] for key in l]
    avg_listify = lambda l: [[arr[0], np.average(np.array(arr[1]))] for arr in l]

    final_data = listify(graph_data)
    final_radar_data = listify(radar_data)
    high_goals_data = listify(high_goals)
    low_goals_data = listify(low_goals)
    climb_data = listify(climb_hash)
    high_avg_data = avg_listify(high_goals_data)
    low_avg_data = avg_listify(low_goals_data)
    climb_avg_data = avg_listify(climb_data)

    sd_high = {}
    sd_low = {}
    sd_climb = {}
    for team in high_goals_data:
        vals = np.array(team[1])

        sd_high.update({team[0]: np.std(vals)})
    for team in low_goals_data:
        vals = np.array(team[1])

        sd_low.update({team[0]: np.std(vals)})
    for team in climb_data:
        vals = np.array(team[1])

        sd_climb.update({team[0]: np.std(vals)})

    sd_high_arr = listify(sd_high)
    sd_low_arr = listify(sd_low)
    sd_climb_arr = listify(sd_climb)

    return render_template('analytics_display.html', 
                len=len(final_data), 
                final_data=final_data, 
                radar_data=final_radar_data, 
                high_goals_data=high_goals_data, 
                low_goals_data=low_goals_data,
                climb_data=climb_data,
                sd_high=sd_high_arr,
                sd_low=sd_low_arr,
                sd_climb=sd_climb_arr,
                high_avg_data=high_avg_data,
                low_avg_data=low_avg_data,
                climb_avg_data=climb_avg_data
                )

@app.route('/analytics_teleop', methods=['GET'])
def analytics_display_teleop():
    return analytics_display('teleop')

@app.route('/analytics_auto', methods=['GET'])
def analytics_display_auto():
    return analytics_display('autonomous')

@app.route('/observing', methods=['GET', 'POST'])
def observation():
    with open('./team_name.txt', 'r') as f:
        name = f.read()

    context = {
        'team_name': name
    }

    if request.method == 'POST':
        for key, val in request.form.items():
            if key == "notes":
                notes = val
             
        # sheet = init_sheet()

        with open('./team_name.txt', 'r') as f:
            name = f.read()

        data = {
            'team_name': name,
            'high_goal': request.json['high_goal'],
            'low_goal': request.json['low_goal'],
            'climb': request.json['climb_points'],
            'penalty': request.json['penalty'],
            'notes': request.json['notes'],
            'defense': request.json['defense'],
            'auto': request.json['auto']
        }

        print(request.json)

        # df = pd.read_csv('./observations/BunnyBots.csv')
        # df = pd.read_csv('./observations/BunnyBots.csv')

        # df = df.append(pd.DataFrame(data), ignore_index=True)

        # df.to_csv('./observations/BunnyBots.csv', index=False) 

        # df = pd.DataFrame(data)

        # df.to_csv(f'./observations/{name}')

        # sheets API update calls
        s_num = 1
        if data['auto']:
            s_num = 2
            data['high_goal'] *= 2
            data['low_goal'] *= 2
            data['climb'] = 0



        sheet = init_sheet(sheet_num=s_num)

        col1 = sheet.col_values(1)
        team_index = len(col1) + 1

        sheet.update_cell(team_index, 1, data['team_name'])
        sheet.update_cell(team_index, 2, data['high_goal'])
        sheet.update_cell(team_index, 3, data['low_goal'])
        sheet.update_cell(team_index, 4, data['climb'])
        sheet.update_cell(team_index, 5, data['penalty'])
        sheet.update_cell(team_index, 6, data['defense'])
        sheet.update_cell(team_index, 7, data['notes'])
            
        # sheet.update_cell(2, 1, name)
        return redirect('home.html')

    if request.method == 'POST':
        if request.form.get('ball_shot'):
            '''
            cell = sheet.cell(2, 2).value
            sheet.update_cell(2, 2, str(int(cell) + 1))
            '''
            balls_shot.value += 1
            
            print(f'{int(balls_shot.value - 1)} -> {int(balls_shot.value)}')
        if request.form.get('accident'):
            accidents.value += 1
            
            print(f'{int(accidents.value - 1)} -> {int(accidents.value)}')
        if request.form.get('e1'):
            e1.value += 1
            
            print(f'{int(e1.value - 1)} -> {int(e1.value)}')
        if request.form.get('e2'):
            e2.value += 1

            print(f'{int(e1.value - 1)} -> {int(e2.value)}')

    return render_template('observing.html', **context) 

if __name__ == '__main__':
    app.run(debug=True)

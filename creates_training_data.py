import pandas
import numpy

def adjust_hero_id(id):
    if id > 108:
        return id - 2
    elif id > 23:
        return id - 1
    else:
        return id

matches = pandas.read_csv('./data/match.csv')
players = pandas.read_csv('./data/players.csv')

arr = [[0 for x in range(221)] for y in range(50000)]
result = pandas.DataFrame(arr)

for i in range(50000):
    row = [0 for _ in range(221)]
    print(i)
    for j in range(5):
        hero_id = players[(players['match_id'] == i) & (players['player_slot'] == j)]['hero_id'].values[0]
        hero_id = adjust_hero_id(hero_id)
        row[hero_id] = 1

    for j in range(128,133):
        hero_id = players[(players['match_id'] == i) & (players['player_slot'] == j)]['hero_id'].values[0]
        hero_id = adjust_hero_id(hero_id)
        row[110 + hero_id] = 1

    if matches[matches['match_id'] == i]['radiant_win'].values[0] == True:
        row[0] = 1
    result.loc[i] = row 
result.to_csv('./data/training_data.csv', index=False)
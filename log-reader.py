import numpy as np
import re

file = 'qgames.log'

death_means = {
  'MOD_UNKNOWN': 'unknown method',
  'MOD_SHOTGUN': 'Shotgun',
  'MOD_GAUNTLET': 'Gauntlet',
  'MOD_MACHINEGUN': 'Machinegun',
  'MOD_GRENADE': 'Grenade',
  'MOD_GRENADE_SPLASH': 'Granede Splash',
  'MOD_ROCKET': 'Rocket',
  'MOD_ROCKET_SPLASH': 'Rocket Splash',
  'MOD_PLASMA': 'Plasma',
  'MOD_PLASMA_SPLASH': 'Planma Splash',
  'MOD_RAILGUN': 'Railgun',
  'MOD_LIGHTNING': 'Lightning',
  'MOD_BFG': 'BFG',
  'MOD_BFG_SPLASH': 'BFG Splash',
  'MOD_WATER': 'Water',
  'MOD_SLIME': 'Slime',
  'MOD_LAVA': 'Lava',
  'MOD_CRUSH': 'Crunch',
  'MOD_TELEFRAG': 'Telefrag',
  'MOD_FALLING': 'Falling',
  'MOD_SUICIDE': 'Kill herself'
}

def kill_parse(read_line: str) -> dict:
  duel = {}
  duel['death_time'] = re.search(r'(\d\:\d{2}|\d{2}\:\d{2})', read_line).group(1)
  duel['player_death'] = re.search(r'killed(.*)by', read_line).group(1).replace(' ', '')
  if '<world>' in read_line:
    duel['mensage_log'] = f'On {duel["death_time"]} The player "{duel["player_death"]}" died because he was wounded and fell from a height enough to kill him.'
  else:
    duel['player_killer'] = re.search(r'\d: (.*)killed', read_line).group(1).replace(' ', '')
    duel['weapon'] = re.search(r'by([\s\S]*)$', read_line).group(1).replace(' ', '')
    duel['mensage_log'] = f'On {duel["death_time"]} The player {duel["player_death"]} was killed by {duel["player_killer"]} using a {death_means[duel["weapon"]]} weapon.'
  return duel

def open_file(file: str) -> list:
  return open(file,'r', encoding='utf-8').readlines()

def find_game_match(data: list) -> dict:
  mach_game={}
  temp_data=[]
  count = 1
  for line in data:
    if line.startswith('  0:00 ------------------------------------------------------------'):
        if temp_data:
          mach_game[f'mach_game_{count}']=temp_data
          count += 1
        temp_data = []
    temp_data.append(line.replace('\n', ""))
    if temp_data:
      mach_game[f'mach_game_{count}']=temp_data

  return mach_game

def find_round_game(data: dict) -> dict:
  make_key_list = list(data.keys())
  temp_data = []
  match_game = {}
  flag=False
  for key in make_key_list:
    list_match_game = data[key]
    count = 1
    round_game = {}
    for line in list_match_game:
      if 'InitGame' in line:
        flag=True
        temp_data.append(line)
      elif line.strip().endswith('ShutdownGame:'):
        flag=False
        if temp_data:
          round_game[f'round_game_log_{count}']=temp_data
          count += 1
        temp_data = []
      elif flag:
        temp_data.append(line)
    match_game[key] = round_game
  return match_game

def parse_data(data: dict) -> dict:
  make_key_list = list(data.keys())
  match_game = {}
  for key in make_key_list:
    list_match_game = list(data[key].keys())
    match_game[key] = {}
    for key_round in list_match_game:
      list_round_game = data[key][key_round]
      match_game[key][key_round] = {}
      match_game[key][key_round]['time_log'] = []
      match_game[key][key_round]['KD'] = {}
      match_game[key][key_round]['weapon_kills'] = {}
      match_game[key][key_round]['total_kills'] = 0
      for line in list_round_game:
        if 'Kill:' in line:
          kill = kill_parse(line)
          match_game[key][key_round]['time_log'].append(kill["mensage_log"])
          if not match_game[key][key_round]['KD'].get(kill["player_death"]):
            match_game[key][key_round]['KD'][kill["player_death"]] = {}
          match_game[key][key_round]['KD'][kill["player_death"]]['deaths'] = match_game[key][key_round]['KD'][kill["player_death"]].get('deaths', 0) + 1
          match_game[key][key_round]['total_kills'] += 1
          if kill.get('player_killer'):
            if not match_game[key][key_round]['KD'].get(kill["player_killer"]): 
              match_game[key][key_round]['KD'][kill["player_killer"]] = {}
            match_game[key][key_round]['KD'][kill["player_killer"]]['kills'] = match_game[key][key_round]['KD'][kill["player_killer"]].get('kills', 0) + 1
            match_game[key][key_round]['total_kills'] += 1

            if not match_game[key][key_round]['weapon_kills'].get(kill["weapon"]):
              match_game[key][key_round]['weapon_kills'][kill["weapon"]] = 0
            match_game[key][key_round]['weapon_kills'][kill["weapon"]] += 1
  return match_game

parse_data(find_round_game(find_game_match(open_file(file=file))))

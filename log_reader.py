import numpy as np
import re

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

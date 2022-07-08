from log_reader import find_round_game, find_game_match
from parse_data import parse_data

file = 'qgames.log'

def open_file(file: str) -> list:
  return open(file,'r', encoding='utf-8').readlines()


print(parse_data(find_round_game(find_game_match(open_file(file=file)))))
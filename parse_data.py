
from helper.parser_info import kill_parse
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
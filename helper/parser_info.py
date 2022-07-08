import re
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

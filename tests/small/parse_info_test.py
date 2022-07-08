import re
from helper.parser_info import kill_parse

def test_kill_parse_wolrd():
  """
  Test kill parse is hable to parse the world kill.
  """
  mock = " 20:54 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT"
  duel = kill_parse(mock)
  result = {'death_time': '20:54', 'player_death': 'Isgalamido', 'mensage_log': 'On 20:54 The player "Isgalamido" died because he was wounded and fell from a height enough to kill him.'}
  assert result == duel

def test_kill_parse_player_kill():
  """
  Test kill parse is hable to parse the player kill.
  """
  mock = " 22:06 Kill: 2 3 7: Isgalamido killed Mocinha by MOD_ROCKET_SPLASH"
  duel = kill_parse(mock)
  print(duel)
  result = {'death_time': '22:06', 'player_death': 'Mocinha', 'player_killer': 'Isgalamido', 'weapon': 'MOD_ROCKET_SPLASH', 'mensage_log': 'On 22:06 The player Mocinha was killed by Isgalamido using a Rocket Splash weapon.'}
  assert result == duel
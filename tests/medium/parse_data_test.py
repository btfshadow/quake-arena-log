import pytest
from parse_data import parse_data
from log_reader import find_game_match, find_round_game

mock = open('tests/medium/qgames.log','r', encoding='utf-8').readlines()
log_reader = find_game_match(mock)
def test_logreader():
    """
    Test if parse_data make de dict.
    """
    data = parse_data(find_round_game(log_reader))
    assert 'time_log' in list(data['mach_game_1']['round_game_log_1'].keys())
    assert 'time_log' in list(data['mach_game_1']['round_game_log_1'].keys())
    assert 'weapon_kills' in list(data['mach_game_1']['round_game_log_1'].keys())
    assert 'total_kills' in list(data['mach_game_1']['round_game_log_1'].keys())
    assert data['mach_game_1']['round_game_log_2']['total_kills'] == 14
    assert data['mach_game_1']['round_game_log_2']['weapon_kills']['MOD_ROCKET_SPLASH'] == 3
    assert 'Mocinha' in list(data['mach_game_1']['round_game_log_2']['KD'].keys())
    assert 'Isgalamido' in list(data['mach_game_1']['round_game_log_2']['KD'].keys())

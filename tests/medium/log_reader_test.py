import pytest
from log_reader import find_game_match, find_round_game

mock = open('tests/medium/qgames.log','r', encoding='utf-8').readlines()

def test_logreader():
    """
    Test if find_game_match find the game match.
    """
    log_reader = find_game_match(mock)
    assert list(log_reader.keys())[0] == 'mach_game_1'
    assert len(log_reader['mach_game_1']) == 97

def test_find_round_game():
    """
    Test if find_round_game find the round of game.
    """
    log_reader = find_game_match(mock)
    data = find_round_game(log_reader)
    assert list(data['mach_game_1'].keys())[0] == 'round_game_log_1'
    assert len(data['mach_game_1']['round_game_log_1']) == 6
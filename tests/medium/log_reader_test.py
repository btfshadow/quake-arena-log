import pytest
from log_reader import find_game_match, find_round_game

mock = open('qgames.log','r', encoding='utf-8').readlines()

def test_logreader():
    log_reader = find_game_match(mock)
    print(log_reader)
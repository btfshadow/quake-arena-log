import pytest
from local_file_reader import  open_file

def test_open_file():
    """
    Test that the file is opened and check his lines.
    """
    file_name = "tests/medium/qgames.log"
    file_handle = open_file(file_name)
    assert len(file_handle) == 5307
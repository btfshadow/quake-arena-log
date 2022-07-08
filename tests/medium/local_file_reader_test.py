import pytest
from local_file_reader import  open_file

def test_open_file():
    """
    Test that the file is opened and closed properly.
    """
    file_name = "qgames.log"
    file_handle = open_file(file_name)
    assert file_handle.closed == False
    file_handle.close()
    assert file_handle.closed == True
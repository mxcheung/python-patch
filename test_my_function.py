from unittest.mock import patch

def my_function():
    return 42

@patch('__main__.my_function')
def test_my_function(mock_function):
    mock_function.return_value = 43
    assert my_function() == 43

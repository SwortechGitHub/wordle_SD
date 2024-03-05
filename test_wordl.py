from main import  check_guess, get_guess, color_word
from unittest.mock import patch

def test_check_guess():
    assert check_guess("Riepa", "Riepa") =="GGGGG"
    assert check_guess("Siena", "anieS") == "YYYYY"
    assert check_guess("reper", "regre") =="GGRYY"
    assert check_guess("anie2", "Siena") == "YYYYR"
    assert check_guess("regr^", "reper") =="GGRYR"

def test_get_guess():
    with patch('builtins.input', return_value='apple'):
        assert get_guess('apple') == 'apple'

    with patch('builtins.input', side_effect=['ap', 'cd', 'abcde']):
        assert get_guess('apple') == 'abcde'

    with patch('builtins.input', side_effect=['APPLE', 'B', 'abcde']):
        assert get_guess('apple') == 'apple'

    with patch('builtins.input', side_effect=['1', '2', 'jinja']):
        assert get_guess('apple') == 'jinja'

    with patch('builtins.input', side_effect=['1263456789','Dāvis']):
        assert get_guess('apple') == 'dāvis'

def test_color_word():
    assert color_word("GGRRY", "apple") == '[green]a[/green][green]p[/green][red]p[/red][red]l[/red][yellow]e[/yellow]'
    assert color_word("GGGGG", "apple") == '[green]a[/green][green]p[/green][green]p[/green][green]l[/green][green]e[/green]'
    assert color_word("GGGGR", "hello") == '[green]h[/green][green]e[/green][green]l[/green][green]l[/green][red]o[/red]'
    assert color_word("RGGGG", "hello") == '[red]h[/red][green]e[/green][green]l[/green][green]l[/green][green]o[/green]'
    assert color_word("YGGGG", "hello") == '[yellow]h[/yellow][green]e[/green][green]l[/green][green]l[/green][green]o[/green]'
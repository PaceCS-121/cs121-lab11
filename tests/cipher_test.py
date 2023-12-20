import solve_cipher
import re

def test_solution(capsys):
    solve_cipher.main()
    captured = capsys.readouterr()
    assert re.match('.*IFATHINGISWORTHDOINGITISWORTHDOINGPOORLY', captured.out, re.IGNORECASE)
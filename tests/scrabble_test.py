import scrabble
import re

def test_lettertile():
    lt = scrabble.LetterTile('A', 1)
    assert lt.get_letter() == 'A'
    assert lt.get_points() == 1
    assert lt.__str__() == 'A'

def test_blanktile():
    bt = scrabble.BlankTile()
    assert bt.get_letter() == '_'
    assert bt.get_points() == 0
    bt.assign_letter('G')
    bt.get_letter() == 'G'

def test_letters():
    letters = scrabble.createLetters()
    assert type(letters) == list
    assert len(letters) == 100
    assert type(letters[0]) == scrabble.LetterTile or type(letters[0]) == scrabble.BlankTile
    tileset = scrabble.chooseTiles(letters)
    assert type(tileset) == list
    assert len(tileset) == 7
    assert type(tileset[0]) == scrabble.LetterTile or type(tileset[0]) == scrabble.BlankTile

def test_main(capsys):
    scrabble.main()
    captured = capsys.readouterr()
    assert len(re.findall(r'((.*[A-Z_].*){7})', captured.out, re.IGNORECASE)) == 2

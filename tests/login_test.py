import re
import login

def test_user(monkeypatch):
    inputs = 'teSt_4321o'
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    u = login.User('jewela', 'Jewel')
    assert u.name == 'Jewel'
    assert u.username == 'jewela'
    u.set_password()
    assert u.password == hash(inputs)
    assert u.login('jewela', 'hi') == False
    assert u.login('jewela', inputs) == True
    
def test_register(monkeypatch):
    inputs = iter(['dbowie', 'david', 'st4rm4nw4it.ng'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    u = login.register()
    assert type(u) == login.User
    assert u.name == 'david'
    assert u.username == 'dbowie'
    assert u.password == hash('st4rm4nw4it.ng')

def test_signin_fail(monkeypatch, capsys):
    # inputs = iter(['dbowie', 'david', 'st4rm4nw4it.ng', 'jewela', 'Jewel', 'teSt_4321o', 'david', 'teSt_4321o'])
    inputs = iter(['dbowie', 'david', 'st4rm4nw4it.ng', 
                   'jewela', 'Jewel', 'teSt_4321o',
                   'wrong', 'wrong'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    login.main()
    captured = capsys.readouterr()
    assert re.search(r'(found|fail|wrong)', captured.out, re.IGNORECASE)

def test_signin_succeed(monkeypatch, capsys):
    # inputs = iter(['dbowie', 'david', 'st4rm4nw4it.ng', 'jewela', 'Jewel', 'teSt_4321o', 'david', 'teSt_4321o'])
    inputs = iter(['dbowie', 'david', 'st4rm4nw4it.ng', 
                   'jewela', 'Jewel', 'teSt_4321o',
                   'dbowie', 'st4rm4nw4it.ng'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    login.main()
    captured = capsys.readouterr()
    assert re.search(r'david', captured.out, re.IGNORECASE)

    
    



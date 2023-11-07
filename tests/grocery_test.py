import grocery

def test_item():
    i = grocery.Item('olives', 6.99)
    assert i.get_name() == 'olives'
    assert i.get_price() == 6.99
    assert type(i.__str__()) == str

def test_expires():
    e = grocery.Expires('eggs', 2.85, '1/1/24')
    assert e.get_name() == 'eggs'
    assert e.get_price() == 2.85
    assert e.get_expiration_date() == '1/1/24'

def test_meat():
    m = grocery.Meat('chicken', 4.69, '12/29/23', 0.75)
    assert m.get_name() == 'chicken'
    assert m.get_weight() == 0.75
    assert m.get_price() == 4.69 * 0.75
from square import square_num,prime

def test_square_num():
    a = 3
    res = square_num(a)
    assert res == 9

def test_prime():
    a = 4
    res = prime(a)
    assert res == "No"
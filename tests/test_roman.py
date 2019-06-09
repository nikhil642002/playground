import RomanConv

def test_roman_1():
    input = 1
    assert RomanConv.to_roman(input) == 'I'

def test_roman_4():
    input = 4
    assert RomanConv.to_roman(input) == 'IV'

def test_roman_5():
    input = 5
    assert RomanConv.to_roman(input) == 'V'

def test_roman_6():
    input = 6
    assert RomanConv.to_roman(input) == 'VI'

def test_roman_4444():
    input = 4444
    assert RomanConv.to_roman(input) == 'MMMMCDXLIV'

def test_roman_9999():
    input = 9999
    assert RomanConv.to_roman(input) == 'MMMMMMMMMCMXCIX'

def test_roman_5555():
    input = 5555
    assert RomanConv.to_roman(input) == 'MMMMMDLV'

def test_roman_4567():
    input = 4567
    assert RomanConv.to_roman(input) == 'MMMMDLXVII'

def test_arabic_1():
    input = 'I'
    assert RomanConv.from_roman(input) == 1


def test_arabic_1():
    input = 'I'
    assert RomanConv.from_roman(input) == 1

def test_arabic_4444():
    input = 'MMMMCDXLIV'
    assert RomanConv.from_roman(input) == 4444

def test_arabic_9999():
    input = 'MMMMMMMMMCMXCIX'
    assert RomanConv.from_roman(input) == 9999

def test_arabic_5555():
    input = 'MMMMMDLV'
    assert RomanConv.from_roman(input) == 5555

def test_arabic_4567():
    input = 'MMMMDLXVII'
    assert RomanConv.from_roman(input) == 4567

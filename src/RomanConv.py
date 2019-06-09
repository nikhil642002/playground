# This was a recent London Python Dojo challenge that wasn't chosen, so I have taken up the challenge
# The task was to create a bidirectional roman numeral converter without using the IF command

def to_roman(number):
    thousands, rest = divmod(number, 1000)
    hundreds, rest = divmod(rest, 100)
    tens, ones = divmod(rest, 10)
    n900s, hrest = divmod(hundreds, 9)
    n500s, hrest = divmod(hrest, 5)
    n400s, hrest = divmod(hrest, 4)
    n90s, trest = divmod(tens, 9)
    n50s, trest = divmod(trest, 5)
    n40s, trest = divmod(trest, 4)
    n9s, nrest = divmod(ones, 9)
    n5s, nrest = divmod(nrest, 5)
    n4s, nrest = divmod(nrest, 4)

    out = "M" * thousands + "CM" * n900s + "D" * n500s + "CD" * n400s + "C" * hrest + "XC" * n90s + "L" * n50s + "XL" * n40s + "X" * trest + "IX" * n9s + "V" * n5s + "IV" * n4s + "I" * nrest

    return out


def from_roman(number):
    four = number.count('IV')
    nine = number.count('IX')
    forty = number.count('XL')
    ninety = number.count('XC')
    fourhun = number.count('CD')
    ninehun = number.count('CM')
    thou = number.count('M') - ninehun
    fivehun = number.count('D') - fourhun
    huns = number.count('C') - fourhun - ninehun - ninety
    fifty = number.count('L') - forty
    tens = number.count('X') - forty - ninety - nine
    five = number.count('V') - four
    ones = number.count('I') - four - nine

    out = 1000 * thou + 100 * huns + 400 * fourhun + 500 * fivehun + 900 * ninehun + 10 * tens + 40 * forty + 50 * fifty + 90 * ninety + ones + 4 * four + 5 * five + 9 * nine

    return out

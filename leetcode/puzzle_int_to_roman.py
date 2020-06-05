def intToRoman(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    result = ""

    for i, v in enumerate(values):
        # get the roman numeral for quotient
        result += (num // v) * roman_numerals[i]
        # get the remainder
        num %= v

    return result

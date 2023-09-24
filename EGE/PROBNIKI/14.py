

def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result


x = 49 ** 7 + 7 ** 20 - 28
ans = convert_to(x,7)
print(ans, str(ans).count("6"))

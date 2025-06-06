from decimal import *

# zadanie 1.
def postal_codes_between(code1, code2):
    codes_numeric = range(int(code1.replace("-", "")) + 1, int(code2.replace("-", "")))

    codes_textual = []

    for code in codes_numeric:
        code_string = str(code).rjust(5, "0")

        code_string = code_string[:2] + "-" + code_string[2:]

        codes_textual.append(code_string)

    return codes_textual

# przykladowe wywolanie    
print(postal_codes_between("79-900", "80-155"))



# zadanie 2.
def missing_elements(number_list, n):
    return [i for i in range(1, n+1) if i not in number_list]

# przykladowe wywolanie
print(missing_elements([2,3,7,4,9], 10))



# zadanie 3.
def generate_list():
    return [i * Decimal(0.5) for i in range(4, 12)]

# przykladowe wywolanie
print(generate_list())
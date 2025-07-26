'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def format_indian_currency(num):
    num_str = str(num)

   
    if '.' in num_str:
        integer_part, decimal_part = num_str.split('.')
        decimal_part = '.' + decimal_part
    else:
        integer_part = num_str
        decimal_part = ''

  
    is_negative = False
    if integer_part.startswith('-'):
        is_negative = True
        integer_part = integer_part[1:]

    if len(integer_part) > 3:
        last_three = integer_part[-3:]
        rest = integer_part[:-3]
        
      
        parts = []
        while len(rest) > 2:
            parts.insert(0, rest[-2:])
            rest = rest[:-2]
        if rest:
            parts.insert(0, rest)

        formatted_integer = ','.join(parts) + ',' + last_three
    else:
        formatted_integer = integer_part

    result = ('-' if is_negative else '') + formatted_integer + decimal_part
    return result


num = float(input("Enter a number: "))
print(format_indian_currency(num))

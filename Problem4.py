'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
n = int(input("Enter number of years: "))
prices = list(map(int, input("Enter space-separated prices: ").split()))


price_to_year = {price: i for i, price in enumerate(prices)}


sorted_prices = sorted(prices)

min_loss = float('inf')
buy_year = sell_year = -1


for i in range(len(sorted_prices)-1, 0, -1):
    higher = sorted_prices[i]
    lower = sorted_prices[i-1]
    
   
    if price_to_year[lower] < price_to_year[higher]:
        loss = higher - lower
        if loss < min_loss:
            min_loss = loss
            buy_year = price_to_year[higher] + 1
            sell_year = price_to_year[lower] + 1

print(f"Buy in year {buy_year}, sell in year {sell_year}, loss = {min_loss}")

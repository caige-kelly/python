for number in range(1, 101):
    fizzbuzz = ""
    if number % 3 == 0:
        fizzbuzz += 'Fizz'
    if number % 5 == 0:
        fizzbuzz += "Buzz"
    if len(fizzbuzz) == 0:
        print(number)
    else:
        print(fizzbuzz)

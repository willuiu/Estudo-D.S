#FizzBuzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(f'{i} É divisivel! FizzBuzz')
    elif i % 3 == 0:
        print(f'{i} É divisivel por 3! Fizz')
    elif i % 5 == 0:
        print(f'{i} É divisivel por 5! Buzz')
    else:
        print(f'{i} Não é divisivel')
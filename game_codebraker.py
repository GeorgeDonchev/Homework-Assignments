import random
digits = list(range(10))
random.shuffle(digits)
number = digits[:3]
print(number)
while True:
    guess = int(input("Please enter your number: "))
    check = int(''.join(map(str,number)))
    if guess == check:
        print("You guessed the number")
        break
    separation = [int(x) for x in str(guess)]
    matches = False
    close = False
    for i in range(len(separation)):
        if separation[i] == number[i]:
            matches = True
        elif separation[i] in number:
            close = True

    if matches and not close:
        print('match')
    elif close and not matches:
        print('close')
    elif close and matches:
        print('match')


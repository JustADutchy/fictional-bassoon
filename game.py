import random
guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well ' + myName + ', I am thinking of a number between 1 and 20.') 

while guessesTaken < 6:
    print('Take a guess.')
    guess = input()
    guess = int(guess)
    
    guessesTaken = guessesTaken + 1
    
    if guess < number:
        print ('Your guess is too low.')
    if guess > number:
        print ('Your guess is too High.')
    if guess == number:
        guessesTaken = str(guessesTaken)
        print ('Nailed it!')
        print ('Nice one ' + myName + ', you guessed the number in ' + guessesTaken + ' guesses!')
        break

if guess != number:
    number = str(number)
    print('Nope. Sad times, i was thinking of the number ' + number)
    

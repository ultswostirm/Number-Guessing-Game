print("Number Guessing Game")
number=5
chances=0
print("Guess a number between 1 and 9->")

while chances<5:
    guess=int(input("Enter your guess: "))

    if guess==number:
        print("Congrats, You Win!!!")
        break
    elif guess>number:
        print("Your guess was too high (Hint: it is a number lesser than 6)")
    else:
        print("Your guess was too low (Hint: it is a number higher than 3)")

        chances+=1 
        if not chances<5:print("You Lost!!!")
        

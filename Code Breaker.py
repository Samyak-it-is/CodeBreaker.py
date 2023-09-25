import random
number=random.randrange(1000,10000)
print(number)
guess=int(input(("What is your guess for the number ?")))
chances=5
if guess==number:
    print("You are a mastermind!!")
else:
    tries=0
    while guess!=number and chances:
        tries+=1
        chances-=1
        rightdigits=0
        guess=str(guess)
        number=str(number)
        correct=["X"]*4
        for i in range(0,4):
            if guess[i]==number[i]:
                rightdigits+=1
                correct[i]=number[i]
        if rightdigits<4 and rightdigits>0 and chances:
            print("Not the right guess but you got the",rightdigits,"right")
            print("Current status is:")
            for char in correct:
                print(char,end="   ")    
            print("\n\n")        
            guess=int(input(("What is your guess for the number ?")))
        elif rightdigits ==0 and chances:
            print("None of the digits you guessed is right")
            guess=int(input(("What is your guess for the number ?")))
    if guess==number:
        print("Great you won in ",tries,"guesses,now you are a mastermind")
    elif chances==0:
            print("Sorry you lost as you ran out of chances")
            print(number,"is the number")
            
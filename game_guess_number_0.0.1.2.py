from random import randint
fate = randint(1,100)
answer = -1
i = 0
print("Guess the number from 1 to 100") 

while answer != fate:
    # Behavior after entering a number
    answer = int(input("Give me a number: "))
    
    if answer > fate:
        print("The drawn number is smaller")
    
    if answer < fate:
        print("The drawn number is greatter")

    # Numbers of filed atempts
    i = i + 1
         
if answer == fate:
    print("You won!!!")
    print("Numbers of wrong guesses",i)

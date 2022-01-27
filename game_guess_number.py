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
    
    # Behavior when the number of unsuccessful attempts equals 10
    if i == 10:
        print("Don't giv up ")
        print("Do you want a hint?")
        print("if so, enter 1 or 2 if not:")
        choice = int(input())
        # Behavior when choice = 1 (Player want a hint)
        if choice == 1:
            if fate > 50:
                print("Your number is anywhere from 1 to 50")
            
            if fate < 50:
                print("Your number is anywhere from 50 to 100")
        # Behavior when choice = 2 (Player don't want a hint)
        if choice == 2:
             answer = int(input("Give me a number: "))
    
             if answer > fate:
                 print("The drawn number is smaller")
    
             if answer < fate:
                print("The drawn number is greatter")

    # Behavior when the number of unsuccessful attempts equals 50
    if i == 50:
        print("Don't giv up ")
        print("Do you want a hint?")
        print("if so, enter 1 or 2 if not:")
        choice = int(input())
        # Behavior when choice = 1 (Player want a hint)
        if choice == 1:
            if 0 < fate < 25:
                print("Your number is anywhere from 1 to 25")
            if 25 < fate < 50:
                print("Your number is anywhere from 25 to 50")
            if 50 < fate < 75:
                print("Your number is anywhere from 50 to 75")
            if 75 < fate < 100:
                print("Your number is anywhere from 75 to 100")
           
        # Behavior when choice = 2 (Player don't want a hint)
        if choice == 2:
             answer = int(input("Give me a number: "))
    
             if answer > fate:
                 print("The drawn number is smaller")
    
             if answer < fate:
                print("The drawn number is greatter")
    if i == 50:
        print("Don't giv up ")
        print("Do you want a hint?")
        print("if so, enter 1 or 2 if not:")
        choice = int(input())
        # Behavior when choice = 1 (Player want a hint)
        if choice == 1:
            if 0 < fate < 25:
                print("Your number is anywhere from 1 to 25")
            if 25 < fate < 50:
                print("Your number is anywhere from 25 to 50")
            if 50 < fate < 75:
                print("Your number is anywhere from 50 to 75")
            if 75 < fate < 100:
                print("Your number is anywhere from 75 to 100")
           
        # Behavior when choice = 2 (Player don't want a hint)
        if choice == 2:
             answer = int(input("Give me a number: "))
    
             if answer > fate:
                 print("The drawn number is smaller")
    
             if answer < fate:
                print("The drawn number is greatter")





   
if answer == fate:
    print("You won!!!")
    print("Numbers of wrong guesses",i)
from random import randint
fate = randint(1,100)
answer = -1
i = 0
def game_easy():
    fate = randint(1,10)
    answer = -1
    i = 0
    print("Guess the number from 1 to 10") 
    
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
            print("if so, enter yes or no if not(without space on the end):")
            choice = str(input())
            # Behavior when choice is yes
            if choice == "yes":
            
                if fate > 50:
                    print("The drawn number is anywhere from 51 to 100")
    
                if fate < 50:
                    print("The drawn number is anywhere from 1 to 50")
        
            # Behavior when choice = 2 (Player don't want a hint)
            if choice == "no":
                answer = int(input("Give me a number: "))
    
                if answer > fate:
                    print("The drawn number is smaller")
    
                if answer < fate:
                    print("The drawn number is greatter")

    if answer == fate:
        print("You won!!!")
    if i == 1:
        print("Numbers of wrong guesses 0")
    if i != 1:
        print("Numbers of wrong guesses",i)
    
    print("___________________________")
        
    print("Do you wana play again?")
    print("if so type yes and if not type no")
    pachoice = str(input())
    if pachoice == "yes":
        print("Do you want to change difficulty mode?")
        print("Is so type yes if not type no(without space on the end)")
        mode_chose_again = str(input())
        if mode_chose_again == "yes":
            print("Choose the difficulty level")
            print("__________________________________")
            print("|easy | medium | hard | imposible|")
            print("----------------------------------")

            print("Type easy if you want to play on easy mode")
            print("Type medium if you want to play on medium mode")
            print("Type hard if you want to play on hard mode")
            print("Type impo if you want to play on imposible mode")
            mode_chose = str(input())
            if mode_chose == "easy":
                game_easy()
            elif mode_chose == "medium":
                game_medium()
            elif mode_chose == "hard":
                game_hard()
            elif mode_chose == "impo":
                game_imposible()
            else:
                print("Something went wrong")
        elif mode_chose_again == "no":
            game_easy()  
    else:
        print("Ok")
        print("Do you want to rate this game?")
        print("If so type yes if not type no (without space on the end)")
        rachoice = input()
        if rachoice == "yes":
            print("Pleas rate this game from 1 to 10")
        elif rachoice == "no":
            print("See you around")
        else:
            print("Somehing went wrong :(")
            print("Are you sure that you typet one of the ones shown?")
            print("You can try once more")
            print("Type only yes or no!(without space on the end)")
            rachoice = input()
            if rachoice == "yes":
                print("Pleas rate this game from 1 to 10")
            elif rachoice == "no":
                print("See you around")
            else:
                print("Somehing went wrong :(")
def game_medium():
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
            print("if so, enter yes or no if not(without space on the end):")
            choice = str(input())
            # Behavior when choice is yes
            if choice == "yes":
            
                if fate > 50:
                    print("The drawn number is anywhere from 51 to 100")
    
                if fate < 50:
                    print("The drawn number is anywhere from 1 to 50")
        
            # Behavior when choice = 2 (Player don't want a hint)
            if choice == "no":
                answer = int(input("Give me a number: "))
    
                if answer > fate:
                    print("The drawn number is smaller")
    
                if answer < fate:
                    print("The drawn number is greatter")

        # Behavior when the number of unsuccessful attempts equals 50
        if i == 50:
            print("Don't giv up ")
            print("Do you want a hint?")
            print("if so, enter yes or no if not (without space on the end):")
            choice = input()
        # Behavior when choice = 1 (Player want a hint)
            if choice == "yes":
                if 0 < fate < 25:
                    print("Your number is anywhere from 1 to 25")
                if 25 < fate < 50:
                    print("Your number is anywhere from 25 to 50")
                if 50 < fate < 75:
                    print("Your number is anywhere from 50 to 75")
                if 75 < fate < 100:
                    print("Your number is anywhere from 75 to 100")
            
            # Behavior when choice = 2 (Player don't want a hint)
            if choice == "no":
                answer = int(input("Give me a number: "))
        
                if answer > fate:
                    print("The drawn number is smaller")
        
                if answer < fate:
                    print("The drawn number is greatter")
        if i == 75:
            print("Don't giv up ")
            print("Do you want a hint?")
            print("if so, enter yes or no if not (without space on the end):")
            choice = input()
            # Behavior when choice = 1 (Player want a hint)
            if choice == "yes":
                if 0 < fate < 5:
                    print("Your number is anywhere from 1 to 5")
                if 5 < fate < 10:
                    print("Your number is anywhere from 5 to 10")
                if 10 < fate < 15:
                    print("Your number is anywhere from 10 to 15")
                if 15 < fate < 20:
                    print("Your number is anywhere from 15 to 20")
                if 20 < fate < 25:
                    print("Your number is anywhere from 20 to 25")
                if 25 < fate < 30:
                    print("Your number is anywhere from 25 to 30")
                if 30 < fate < 35:
                    print("Your number is anywhere from 30 to 35")
                if 35 < fate < 40:
                    print("Your number is anywhere from 35 to 40")
                if 40 < fate < 45:
                    print("Your number is anywhere from 40 to 45")
                if 45 < fate < 50:
                    print("Your number is anywhere from 45 to 50")
                if 50 < fate < 55:
                    print("Your number is anywhere from 50 to 55")
                if 55 < fate < 60:
                    print("Your number is anywhere from 55 to 60")
                if 60 < fate < 65:
                    print("Your number is anywhere from 60 to 65")
                if 65 < fate < 70:
                    print("Your number is anywhere from 65 to 70")
                if 70 < fate < 75:
                    print("Your number is anywhere from 70 to 75")
                if 75 < fate < 80:
                    print("Your number is anywhere from 75 to 80")
                if 80 < fate < 85:
                    print("Your number is anywhere from 80 to 85")
                if 85 < fate < 90:
                    print("Your number is anywhere from 85 to 90")
                if 95 < fate < 100:
                    print("Your number is anywhere from 95 to 100")
            # Behavior when choice = 2 (Player don't want a hint)
            if choice == "no":
                answer = int(input("Give me a number: "))
        
                if answer > fate:
                    print("The drawn number is smaller")
        
                if answer < fate:
                    print("The drawn number is greatter")
    if answer == fate:
        print("You won!!!")
    if i == 1:
        print("Numbers of wrong guesses 0")
    if i != 1:
        print("Numbers of wrong guesses",i)
    
    print("___________________________")
        
    print("Do you wana play again?")
    print("if so type 1 and if not type 2")
    pachoice = int(input())
    if pachoice == 1:
        print("Do you want to change difficulty mode?")
        print("Is so type yes if not type no(without space on the end)")
        mode_chose_again = str(input())
        if mode_chose_again == "yes":
            print("Choose the difficulty level")
            print("__________________________________")
            print("|easy | medium | hard | imposible|")
            print("----------------------------------")

            print("Type easy if you want to play on easy mode")
            print("Type medium if you want to play on medium mode")
            print("Type hard if you want to play on hard mode")
            print("Type impo if you want to play on imposible mode")
            mode_chose = str(input())
            if mode_chose == "easy":
                game_easy()
            elif mode_chose == "medium":
                game_medium()
            elif mode_chose == "hard":
                game_hard()
            elif mode_chose == "impo":
                game_imposible()
            else:
                print("Something went wrong")
        elif mode_chose_again == "no":
            game_medium()  
    else:
        print("Ok")
        print("Do you want to rate this game?")
        print("If so type yes if not type no (without space on the end)")
        rachoice = input()
        if rachoice == "yes":
            print("Pleas rate this game from 1 to 10")
        elif rachoice == "no":
            print("See you around")
        else:
            print("Somehing went wrong :(")
            print("Are you sure that you typet one of the ones shown?")
            print("You can try once more")
            print("Type only yes or no!(without space on the end)")
            rachoice = input()
            if rachoice == "yes":
                print("Pleas rate this game from 1 to 10")
            elif rachoice == "no":
                print("See you around")
            else:
                print("Somehing went wrong :(")
def game_hard():
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
        
        # Behavior when the number of unsuccessful attempts equals 50
        if i == 50:
            print("Don't giv up ")
            print("Do you want a hint?")
            print("if so, enter yes or no if not (without space on the end):")
            choice = input()
        # Behavior when choice = 1 (Player want a hint)
            if choice == "yes":
                if 0 < fate < 25:
                    print("Your number is anywhere from 1 to 25")
                if 25 < fate < 50:
                    print("Your number is anywhere from 25 to 50")
                if 50 < fate < 75:
                    print("Your number is anywhere from 50 to 75")
                if 75 < fate < 100:
                    print("Your number is anywhere from 75 to 100")
            
            # Behavior when choice = 2 (Player don't want a hint)
            if choice == "no":
                answer = int(input("Give me a number: "))
        
                if answer > fate:
                    print("The drawn number is smaller")
        
                if answer < fate:
                    print("The drawn number is greatter")
        if i == 75:
            print("Don't giv up ")
            print("Do you want a hint?")
            print("if so, enter yes or no if not (without space on the end):")
            choice = input()
            # Behavior when choice = 1 (Player want a hint)
            if choice == "yes":
                if 0 < fate < 5:
                    print("Your number is anywhere from 1 to 5")
                if 5 < fate < 10:
                    print("Your number is anywhere from 5 to 10")
                if 10 < fate < 15:
                    print("Your number is anywhere from 10 to 15")
                if 15 < fate < 20:
                    print("Your number is anywhere from 15 to 20")
                if 20 < fate < 25:
                    print("Your number is anywhere from 20 to 25")
                if 25 < fate < 30:
                    print("Your number is anywhere from 25 to 30")
                if 30 < fate < 35:
                    print("Your number is anywhere from 30 to 35")
                if 35 < fate < 40:
                    print("Your number is anywhere from 35 to 40")
                if 40 < fate < 45:
                    print("Your number is anywhere from 40 to 45")
                if 45 < fate < 50:
                    print("Your number is anywhere from 45 to 50")
                if 50 < fate < 55:
                    print("Your number is anywhere from 50 to 55")
                if 55 < fate < 60:
                    print("Your number is anywhere from 55 to 60")
                if 60 < fate < 65:
                    print("Your number is anywhere from 60 to 65")
                if 65 < fate < 70:
                    print("Your number is anywhere from 65 to 70")
                if 70 < fate < 75:
                    print("Your number is anywhere from 70 to 75")
                if 75 < fate < 80:
                    print("Your number is anywhere from 75 to 80")
                if 80 < fate < 85:
                    print("Your number is anywhere from 80 to 85")
                if 85 < fate < 90:
                    print("Your number is anywhere from 85 to 90")
                if 95 < fate < 100:
                    print("Your number is anywhere from 95 to 100")
            # Behavior when choice = 2 (Player don't want a hint)
            if choice == "no":
                answer = int(input("Give me a number: "))
        
                if answer > fate:
                    print("The drawn number is smaller")
        
                if answer < fate:
                    print("The drawn number is greatter")
    if answer == fate:
        print("You won!!!")
    if i == 1:
        print("Numbers of wrong guesses 0")
    if i != 1:
        print("Numbers of wrong guesses",i)
    
    print("___________________________")
        
    print("Do you wana play again?")
    print("if so type 1 and if not type 2")
    pachoice = int(input())
    if pachoice == 1:
        print("Do you want to change difficulty mode?")
        print("Is so type yes if not type no(without space on the end)")
        mode_chose_again = str(input())
        if mode_chose_again == "yes":
            print("Choose the difficulty level")
            print("__________________________________")
            print("|easy | medium | hard | imposible|")
            print("----------------------------------")

            print("Type easy if you want to play on easy mode")
            print("Type medium if you want to play on medium mode")
            print("Type hard if you want to play on hard mode")
            print("Type impo if you want to play on imposible mode")
            mode_chose = str(input())
            if mode_chose == "easy":
                game_easy()
            elif mode_chose == "medium":
                game_medium()
            elif mode_chose == "hard":
                game_hard()
            elif mode_chose == "impo":
                game_imposible()
            else:
                print("Something went wrong")
        elif mode_chose_again == "no":
            game_hard()  
    else:
        print("Ok")
        print("Do you want to rate this game?")
        print("If so type yes if not type no (without space on the end)")
        rachoice = input()
        if rachoice == "yes":
            print("Pleas rate this game from 1 to 10")
        elif rachoice == "no":
            print("See you around")
        else:
            print("Somehing went wrong :(")
            print("Are you sure that you typet one of the ones shown?")
            print("You can try once more")
            print("Type only yes or no!(without space on the end)")
            rachoice = input()
            if rachoice == "yes":
                print("Pleas rate this game from 1 to 10")
            elif rachoice == "no":
                print("See you around")
            else:
                print("Somehing went wrong :(")
def game_imposible():
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
    if i == 1:
        print("Numbers of wrong guesses 0")
    if i != 1:
        print("Numbers of wrong guesses",i)
    
    print("___________________________")
        
    print("Do you wana play again?")
    print("if so type 1 and if not type 2")
    pachoice = int(input())
    if pachoice == 1:
        print("Do you want to change difficulty mode?")
        print("Is so type yes if not type no(without space on the end)")
        mode_chose_again = str(input())
        if mode_chose_again == "yes":
            print("Choose the difficulty level")
            print("__________________________________")
            print("|easy | medium | hard | imposible|")
            print("----------------------------------")

            print("Type easy if you want to play on easy mode")
            print("Type medium if you want to play on medium mode")
            print("Type hard if you want to play on hard mode")
            print("Type impo if you want to play on imposible mode")
            mode_chose = str(input())
            if mode_chose == "easy":
                game_easy()
            elif mode_chose == "medium":
                game_medium()
            elif mode_chose == "hard":
                game_hard()
            elif mode_chose == "impo":
                game_imposible()
            else:
                print("Something went wrong")
        elif mode_chose_again == "no":
            game_easy()  
    else:
        print("Ok")
        print("Do you want to rate this game?")
        print("If so type yes if not type no (without space on the end)")
        rachoice = input()
        if rachoice == "yes":
            print("Pleas rate this game from 1 to 10")
        elif rachoice == "no":
            print("See you around")
        else:
            print("Somehing went wrong :(")
            print("Are you sure that you typet one of the ones shown?")
            print("You can try once more")
            print("Type only yes or no!(without space on the end)")
            rachoice = input()
            if rachoice == "yes":
                print("Pleas rate this game from 1 to 10")
            elif rachoice == "no":
                print("See you around")
            else:
                print("Somehing went wrong :(")             

print("Choose the difficulty level")
print("____________________________________")
print("| Easy | Medium | Hard | iImposible |")
print("------------------------------------")

print("Type easy if you want to play on easy mode")
print("Type medium if you want to play on medium mode")
print("Type hard if you want to play on hard mode")
print("Type impo if you want to play on imposible mode")

mode_chose = str(input())
if mode_chose == "easy":
    game_easy()
elif mode_chose == "medium":
    game_medium()
elif mode_chose == "hard":
    game_hard()
elif mode_chose == "impo":
    game_imposible()
else:
    print("Something went wrong")

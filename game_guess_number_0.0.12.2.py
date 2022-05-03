from random import randint
from time import sleep
fate = randint(1,100)
answer = -1
i = 0
q = 0
def hint_one():
    print("Don't giv up ")
    print("Do you want a hint?")
    print("if so, enter yes or no if not:")
    choice = str(input())
    # Behavior when choice is yes
    if choice == "yes" or "YES" or "yes " or "Yes" or "YES " or "Yes ":
            
        if fate > 50:
            print("The drawn number is anywhere from 51 to 100")
    
        if fate < 50:
            print("The drawn number is anywhere from 1 to 50")
        
        # Behavior when choice = 2 (Player don't want a hint)
        if choice == "no" or "NO" or "no " or "NO " or "No" or "No ":
            answer = int(input("Give me a number: "))
    
            if answer > fate:
                print("The drawn number is smaller")
    
            if answer < fate:
                print("The drawn number is greatter")
def hint_two():
    print("Don't giv up ")
    print("Do you want a hint?")
    print("if so, enter yes or no if not:")
    choice = input()
    # Behavior when choice = 1 (Player want a hint)
    if choice == "yes" or "YES" or "yes " or "Yes" or "YES " or "Yes ":
        if 0 < fate < 25:
            print("Your number is anywhere from 1 to 25")
        if 25 < fate < 50:
            print("Your number is anywhere from 25 to 50")
        if 50 < fate < 75:
            print("Your number is anywhere from 50 to 75")
        if 75 < fate < 100:
            print("Your number is anywhere from 75 to 100")
            
        # Behavior when choice = 2 (Player don't want a hint)
        if choice == "no" or "NO" or "no " or "NO " or "No" or "No ":
            answer = int(input("Give me a number: "))
        
            if answer > fate:
                print("The drawn number is smaller")
        
            if answer < fate:
                print("The drawn number is greatter")
def hint_three():
    print("Don't giv up ")
    print("Do you want a hint?")
    print("if so, enter yes or no if not:")
    choice = input()
    # Behavior when choice = 1 (Player want a hint)
    if choice == "yes" or "YES" or "yes " or "Yes" or "YES " or "Yes ":
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
    if choice == "no" or "NO" or "no " or "NO " or "No" or "No ":
        answer = int(input("Give me a number: "))
        
        if answer > fate:
            print("The drawn number is smaller")
        
        if answer < fate:
            print("The drawn number is greatter")    

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
            hint_one()
           

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
    if pachoice == "yes" or "YES" or "yes " or "Yes" or "YES " or "Yes ":
        print("Do you want to change difficulty mode?")
        print("Is so type yes if not type no")
        mode_chose_again = str(input())
        if mode_chose_again == "yes" or "YES" or "yes " or "Yes" or "YES " or "Yes ":
            dif_levels()
        elif mode_chose_again == "no" or "NO" or "no " or "NO " or "No" or "No ":
            game_easy()  
    else:
        print("Ok")
        print("Do you want to rate this game?")
        print("If so type yes if not type no")
        rachoice = str(input())
        if rachoice == "yes" or "YES" or "yes " or "Yes" or "YES " or "Yes ":
            print("Pleas rate this game from 1 to 10")
        elif rachoice == "no" or "NO" or "no " or "NO " or "No" or "No ":
            print("See you around")
        else:
            print("Somehing went wrong :(")
            print("Are you sure that you typet one of the ones shown?")
            print("You can try once more")
            print("Type only yes or no!")
            rachoice = input()
            if rachoice == "yes" or "YES" or "yes " or "Yes" or "YES " or "Yes ":
                print("Pleas rate this game from 1 to 10")
            elif rachoice == "no" or "NO" or "no " or "NO " or "No" or "No ":
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
            hint_one()

        # Behavior when the number of unsuccessful attempts equals 50
        if i == 50:
            hint_two()
        if i == 75:
           hint_three()
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
        print("Is so type yes if not type no")
        mode_chose_again = str(input())
        if mode_chose_again == "yes" or "YES" or "yes " or "Yes" or "YES " or "Yes ":
            dif_levels()
        elif mode_chose_again == "no" or "NO" or "no " or "NO " or "No" or "No ":
            game_medium()  
    else:
        print("Ok")
        print("Do you want to rate this game?")
        print("If so type yes if not type no")
        rachoice = input()
        if rachoice == "yes" or "YES" or "yes " or "Yes" or "YES " or "Yes ":
            print("Pleas rate this game from 1 to 10")
        elif rachoice == "no" or "NO" or "no " or "NO " or "No" or "No ":
            print("See you around")
        else:
            print("Somehing went wrong :(")
            print("Are you sure that you typet one of the ones shown?")
            print("You can try once more")
            print("Type only yes or no!")
            rachoice = input()
            if rachoice == "yes" or "YES" or "yes " or "Yes" or "YES " or "Yes ":
                print("Pleas rate this game from 1 to 10")
            elif rachoice == "no" or "NO" or "no " or "NO " or "No" or "No ":
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
            hint_two()
        if i == 75:
            hint_three()
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
        print("Is so type yes if not type no")
        mode_chose_again = str(input())
        if mode_chose_again == "yes" or "YES" or "yes " or "Yes" or "YES " or "Yes ":
           dif_levels()
        elif mode_chose_again == "no" or "NO" or "no " or "NO " or "No" or "No ":
            game_hard()  
    else:
        print("Ok")
        print("Do you want to rate this game?")
        print("If so type yes if not type no")
        rachoice = input()
        if rachoice == "yes" or "YES" or "yes " or "Yes" or "YES " or "Yes ":
            print("Pleas rate this game from 1 to 10")
        elif rachoice == "no" or "NO" or "no " or "NO " or "No" or "No ":
            print("See you around")
        else:
            print("Somehing went wrong :(")
            print("Are you sure that you typet one of the ones shown?")
            print("You can try once more")
            print("Type only yes or no!")
            rachoice = input()
            if rachoice == "yes" or "YES" or "yes " or "Yes" or "YES " or "Yes ":
                print("Pleas rate this game from 1 to 10")
            elif rachoice == "no" or "NO" or "no " or "NO " or "No" or "No ":
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
        print("Is so type yes if not type no")
        mode_chose_again = str(input())
        if mode_chose_again == "yes" or "YES" or "yes " or "Yes" or "YES " or "Yes ":
           dif_levels()
        elif mode_chose_again == "no" or "NO" or "no " or "NO " or "No" or "No ":
            game_easy()  
    else:
        print("Ok")
        print("Do you want to rate this game?")
        print("If so type yes if not type no")
        rachoice = input()
        if rachoice == "yes" or "YES" or "yes " or "Yes" or "YES " or "Yes ":
            print("Pleas rate this game from 1 to 10")
        elif rachoice == "no" or "NO" or "no " or "NO " or "No" or "No ":
            print("See you around")
        else:
            print("Somehing went wrong :(")
            print("Are you sure that you typet one of the ones shown?")
            print("You can try once more")
            print("Type only yes or no!")
            rachoice = input()
            if rachoice == "yes" or "YES" or "yes " or "Yes" or "YES " or "Yes ":
                print("Pleas rate this game from 1 to 10")
            elif rachoice == "no" or "NO" or "no " or "NO " or "No" or "No ":
                print("See you around")
            else:
                print("Somehing went wrong :(")             

def easy_info():
    print("|Easy gameplay. Number from 1 to 10|")
def medium_info():
    print("|Casual game play. Number from 1 to 100            |")
    print("|You have 3 hint. On 10, 50 ,75 wrong guesses      |")
    print("|also if typed number is wrong you see             | ")
    print("|whether it is greater or less than the one entered|")
def hard_info():
    print("|Harder then normal.Number from 1 to 100|")
    print("|but you only have 2 hints on 50 and 75 |")
def impo_info():
    print("|Very very hard gameplay. 0 hints and greater or smaller|")

def info():
    print("Information about dificulty levels")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    sleep(1)
    print("Type easy-info if you want to info about easy mode")
    sleep(0.1)
    print("Type medium-info if you want to info about medium mode")
    sleep(0.1)
    print("Type hard-info if you want to info about hard mode")
    sleep(0.1)
    print("Type impo-info if you want to info about imposible mode")
    sleep(0.1)
    print("Type return to return to chosing difficulty level screen")
    sleep(0.1)
    info_choice = str(input())
    if info_choice == "easy-info":
        sleep(0.5)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        easy_info()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        info()
    elif info_choice == "medium-info":
        sleep(0.5)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        medium_info()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        info()
    elif info_choice == "hard-info":
        sleep(0.5)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        hard_info()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        info()
    elif info_choice == "impo-info":
        sleep(0.5)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        impo_info()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        info()
    elif info_choice == "return":
        
        sleep(0.5)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        dif_levels() 

def dif_levels():
    print("Choose the difficulty level")
    sleep(0.1)
    print("____________________________________")
    sleep(0.1)
    print("| Easy | Medium | Hard | Imposible |")
    sleep(0.1)
    print("------------------------------------")
    sleep(0.5)

    print("Type easy if you want to play on easy mode")
    sleep(0.1)
    print("Type medium if you want to play on medium mode")
    sleep(0.1)
    print("Type hard if you want to play on hard mode")
    sleep(0.1)
    print("Type impo if you want to play on imposible mode")
    sleep(0.1)
    print("_________________________________________________")
    sleep(0.1)
    print("Type info if you want to get mor information about difficulty levels")
    

    mode_chose = str(input())
    if mode_chose == "easy":
        game_easy()
    elif mode_chose == "medium":
        game_medium()
    elif mode_chose == "hard":
        game_hard()
    elif mode_chose == "impo":
        game_imposible()
    elif mode_chose == "info":
        info()
    else:
        print("Something went wrong")


    
def game_start():
    print("                                                                                                 ")
    sleep(0.1)
    print("░██████╗░██╗░░░██╗███████╗░██████╗░██████╗  ███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░")
    sleep(0.1)
    print("██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝  ████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗")
    sleep(0.1)
    print("██║░░██╗░██║░░░██║█████╗░░╚█████╗░╚█████╗░  ██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝")
    sleep(0.1)
    print("██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗░╚═══██╗  ██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗")
    sleep(0.1)
    print("╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝  ██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║")
    sleep(0.1)
    print("                                                                                                 ")
    sleep(0.1)
    print("                         ░██████╗░░█████╗░███╗░░░███╗███████╗                                    ")
    sleep(0.1)
    print("                         ██╔════╝░██╔══██╗████╗░████║██╔════╝                                    ")
    sleep(0.1)
    print("                         ██║░░██╗░███████║██╔████╔██║█████╗░░                                    ")
    sleep(0.1)
    print("                         ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░                                    ")
    sleep(0.1)
    print("                         ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗                                    ")
    sleep(0.1)
    print("                         ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝                                    ")
    sleep(0.1)
    print("                                                                                                 ")
    sleep(0.1)
    print("                                                                                                 ")
    sleep(0.3)
    print("                              TYPE START TO START THE GAME                                       ")
    start_choice = str(input())
    if start_choice == "START":
        sleep(2)
        dif_levels()

game_start()

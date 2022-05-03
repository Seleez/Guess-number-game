from random import randint
from time import sleep
from tkinter.font import BOLD
import turtle 
fate = randint(1,100)
answer = -1
i = 0
c = 0
t = turtle.Turtle()
t_clean = turtle.Turtle()
wn = turtle.Screen()
wn.title("Guess Number Game")
wn.bgcolor('black')
wn.setup(width = 1000, height = 760)
wn.tracer(0)
def clean():
    t_clean.goto(-500,380)
    t_clean.color('black')
    t_clean.begin_fill()
    t_clean.forward(1000)
    t_clean.right(90)
    t_clean.forward(1000)
    t_clean.right(90)
    t_clean.forward(1000)
    t_clean.right(90)
    t_clean.forward(1000)
    t_clean.right(90)
    t_clean.end_fill()
def hint_one():
    t.goto(-500,340)
    t.write("Don't give up ")
    t.forward(15)
    t.write("Do you want a hint?")
    t.forward(15)
    t.write("if so, enter yes or no if not:")
    t.forward(15)
    choice = turtle.textinput('Choice', 'Type yes or no ')
    # Behavior when choice is yes
    if choice == "yes" or "YES" or "yes " or "Yes" or "YES " or "Yes ":
            
        if fate > 50:
            t.write("The drawn number is anywhere from 51 to 100")
            t.forward(15)
    
        if fate < 50:
            t.write("The drawn number is anywhere from 1 to 50")
            t.forward(15)
        
        # Behavior when choice = 2 (Player don't want a hint)
        if choice == "no" or "NO" or "no " or "NO " or "No" or "No ":
            answer = turtle.textinput('Your guess', 'Type your number.')
    
            if answer > fate:
               t.write("The drawn number is smaller")
               t.forward(15)
    
            if answer < fate:
                t.write("The drawn number is greatter")
                t.forward(15)
    clean()
def hint_two():
    t.write("Don't give up ")
    t.write("Do you want a hint?")
    t.write("if so, enter yes or no if not:")
    choice = turtle.textinput('Choice', 'Type yes or no ')
    # Behavior when choice = 1 (Player want a hint)
    if choice == "yes" or "YES" or "yes " or "Yes" or "YES " or "Yes ":
        if 0 < fate < 25:
            t.write("Your number is anywhere from 1 to 25")
        if 25 < fate < 50:
            t.write("Your number is anywhere from 25 to 50")
        if 50 < fate < 75:
            t.write("Your number is anywhere from 50 to 75")
        if 75 < fate < 100:
            t.write("Your number is anywhere from 75 to 100")
            
        # Behavior when choice = 2 (Player don't want a hint)
        if choice == "no" or "NO" or "no " or "NO " or "No" or "No ":
            answer = turtle.numinput('Choice', 'Type yes or no ')
        
            if answer > fate:
                t.write("The drawn number is smaller")
        
            if answer < fate:
               t.write("The drawn number is greatter")
def hint_three():
    t.write("Don't giv up ")
    t.write("Do you want a hint?")
    t.write("if so, enter yes or no if not:")
    choice = turtle.textinput('Choice', 'Type yes or no ')
    # Behavior when choice = 1 (Player want a hint)
    if choice == "yes" or "YES" or "yes " or "Yes" or "YES " or "Yes ":
            if 0 < fate < 5:
                t.write("Your number is anywhere from 1 to 5")
            if 5 < fate < 10:
                t.write("Your number is anywhere from 5 to 10")
            if 10 < fate < 15:
                t.write("Your number is anywhere from 10 to 15")
            if 15 < fate < 20:
                t.write("Your number is anywhere from 15 to 20")
            if 20 < fate < 25:
                t.write("Your number is anywhere from 20 to 25")
            if 25 < fate < 30:
                t.write("Your number is anywhere from 25 to 30")
            if 30 < fate < 35:
                t.write("Your number is anywhere from 30 to 35")
            if 35 < fate < 40:
                t.write("Your number is anywhere from 35 to 40")
            if 40 < fate < 45:
                t.write("Your number is anywhere from 40 to 45")
            if 45 < fate < 50:
                t.write("Your number is anywhere from 45 to 50")
            if 50 < fate < 55:
                t.write("Your number is anywhere from 50 to 55")
            if 55 < fate < 60:
                t.write("Your number is anywhere from 55 to 60")
            if 60 < fate < 65:
                t.write("Your number is anywhere from 60 to 65")
            if 65 < fate < 70:
                t.write("Your number is anywhere from 65 to 70")
            if 70 < fate < 75:
                t.write("Your number is anywhere from 70 to 75")
            if 75 < fate < 80:
                t.write("Your number is anywhere from 75 to 80")
            if 80 < fate < 85:
                t.write("Your number is anywhere from 80 to 85")
            if 85 < fate < 90:
                t.write("Your number is anywhere from 85 to 90")
            if 95 < fate < 100:
                t.write("Your number is anywhere from 95 to 100")
    # Behavior when choice = 2 (Player don't want a hint)
    if choice == "no" or "NO" or "no " or "NO " or "No" or "No ":
        answer = turtle.numinput('Choice', 'Type yes or no ')
        
        if answer > fate:
            t.write("The drawn number is smaller")
        
        if answer < fate:
            t.write("The drawn number is greatter")    

def play_again():
    t.write("Do you wana play again?")
    t.forward(15)
    t.write("if so type yes and if not type no")
    t.forward(15)
    pachoice = turtle.textinput('Choice', 'Wat do you want to do')
    if pachoice == "yes" or "YES" or "yes " or "Yes" or "YES " or "Yes ":
        t.write("Do you want to change difficulty mode?")
        t.forward(15)
        t.write("Is so type yes if not type no")
        t.forward(15)
        mode_chose_again = turtle.textinput('Choice', 'Wat do you want to do')
        if mode_chose_again == "yes" or "YES" or "yes " or "Yes" or "YES " or "Yes ":
            dif_levels()
        elif mode_chose_again == "no" or "NO" or "no " or "NO " or "No" or "No ":
            game_easy()  
    else:
        ("Ok")
        t.write("Do you want to rate this game?")
        t.forward(15)
        t.write("If so type yes if not type no")
        t.forward(15)
        rachoice = turtle.textinput('Choice', 'Wat do you want to do')
        if rachoice == "yes" or "YES" or "yes " or "Yes" or "YES " or "Yes ":
            t.write("Pleas rate this game from 1 to 10")
            t.forward(15)
        elif rachoice == "no" or "NO" or "no " or "NO " or "No" or "No ":
            t.write("See you around")
            t.forward(15)
        else:
            t.write("Somehing went wrong :(")
            t.forward(15)
            t.writet("Are you sure that you typet one of the ones shown?")
            t.forward(15)
            t.write("You can try once more")
            t.forward(15)
            t.write("Type only yes or no!")
            t.forward(15)
            rachoice = turtle.textinput('Choice', 'Wat do you want to do')
            if rachoice == "yes" or "YES" or "yes " or "Yes" or "YES " or "Yes ":
                t.write("Pleas rate this game from 1 to 10")
                t.forward(15)
            elif rachoice == "no" or "NO" or "no " or "NO " or "No" or "No ":
                t.write("See you around")
                t.forward(15)
            else:
                t.write("Somehing went wrong :(")

def game_easy():
    fate = randint(1,10)
    answer = -1
    i = 0
    c = 0
    t.write("Guess the number from 1 to 10")
    t.goto(-500,340)
    while answer != fate:
        c = c + 1
        # Behavior after entering a number
        answer = turtle.numinput('Your guess', 'Type your number.')

        if answer > fate:
            t.write("The drawn number is smaller")
            t.forward(15)
    
        if answer < fate:
            t.write("The drawn number is greatter")
            t.forward(15)

        # Numbers of filed atempts
        i = i + 1
    
        # Behavior when the number of unsuccessful attempts equals 10
        if i == 10:
            hint_one()
        if c == 10:
            clean()
            c = 0
            t.goto(-500,340)
           

    if answer == fate:
        t.write("You won!!!")
        t.forward(15)
    if i == 1:
        t.write("Numbers of wrong guesses 0")
        t.forward(15)
    if i != 1:
       t.write("Numbers of wrong guesses", i)
       t.forward(15)
    
    t.write("___________________________")
    play_again()       
def game_medium():
    fate = randint(1,100)
    answer = -1
    i = 0
    c = 0
    t.goto(-500,340)
    t.write("Guess the number from 1 to 100")
    t.forward(15) 
    while answer != fate:
        c = c + 1
        # Behavior after entering a number
        answer = turtle.numinput('Your guess', 'Type your number.')

        if answer > fate:
            t.write("The drawn number is smaller")
            t.forward(15)
    
        if answer < fate:
           t.write("The drawn number is greatter")
           t.forward(15)

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
           if c == 10:
               clean()
               c = 0
               t.goto(-500,340)
    if answer == fate:
        t.write("You won!!!")
        t.forward(15)
    if i == 1:
        t.write("Numbers of wrong guesses 0")
        t.forward(15)
    if i != 1:
        t.write("Numbers of wrong guesses",i)
        t.forward(15)
    
    t.write("___________________________")
    t.forward(15)
        
    play_again()
def game_hard():
    fate = randint(1,100)
    answer = -1
    i = 0
    c = 0
    t.goto(-500,340)
    t.write("Guess the number from 1 to 100") 
    while answer != fate:
        c = c + 1
        # Behavior after entering a number
        answer = turtle.numinput('Your guess', 'Type your number.')

        if answer > fate:
            t.write("The drawn number is smaller")
            t.forward(15)
    
        if answer < fate:
            t.write("The drawn number is greatter")
            t.forward(15)

        # Numbers of filed atempts
        i = i + 1
    
        # Behavior when the number of unsuccessful attempts equals 10
        
        # Behavior when the number of unsuccessful attempts equals 50
        if i == 50:
            hint_two()
            t.forward(15)
        if i == 75:
            hint_three()
            t.forward(15)
            if c == 10:
                clean()
                c = 0
                t.goto(-500,340)
    if answer == fate:
        t.write("You won!!!")
        t.forward(15)
    if i == 1:
        t.write("Numbers of wrong guesses 0")
        t.forward(15)
    if i != 1:
        t.write("Numbers of wrong guesses",i)
        t.forward(15)
    
    t.write("___________________________")
    t.forward(15)
        
    play_again()
def game_imposible():
    fate = randint(1,100)
    answer = -1
    i = 0
    c = 0
    t.goto(-500,340)
    t.write("Guess the number from 1 to 100") 
    t.forward(15)
    while answer != fate:
        # Behavior after entering a number
        answer = turtle.numinput('Your guess', 'Type your number.')
        t.forward(15)

        if answer > fate:
            t.write("The drawn number is smaller")
            t.forward(15)
    
        if answer < fate:
            t.write("The drawn number is greatter")
            t.forward(15)

        # Numbers of filed atempts
        i = i + 1
         
    if answer == fate:
        t.write("You won!!!")
        t.forward(15)
    if i == 1:
        t.write("Numbers of wrong guesses 0")
        t.forward(15)
    if i != 1:
        t.write("Numbers of wrong guesses",i)

    
    t.write("___________________________")
        
    play_again()             

def easy_info():
    t.write("|Easy gameplay. Number from 1 to 10|")
    clean()
def medium_info():
    t.write('|Casual game play. Number from 1 to 100            |')
    t.write('|You have 3 hint. On 10, 50 ,75 wrong guesses      |')
    t.write('|also if typed number is wrong you see             |')
    t.write('|whether it is greater or less than the one entered|')
    clean()
def hard_info():
    t.write('|Harder then normal.Number from 1 to 100|')
    t.write('|but you only have 2 hints on 50 and 75 |')
    clean()
def impo_info():
    t.write('|Very very hard gameplay. 0 hints and greater or smaller|')
    clean()
def info():
    t.goto(-500,340)
    sleep(0.2)
    t.write("Information about dificulty levels")
    t.forward(20)
    sleep(0.1)
    t.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    t.forward(20)
    sleep(1)
    t.write("Type easy-info if you want to info about easy mode")
    t.forward(20)
    sleep(0.1)
    t.write("Type medium-info if you want to info about medium mode")
    t.forward(20)
    sleep(0.1)
    t.write("Type hard-info if you want to info about hard mode")
    t.forward(20)
    sleep(0.1)
    t.write("Type impo-info if you want to info about imposible mode")
    t.forward(20)
    sleep(0.1)
    t.write("Type return to return to chosing difficulty level screen")
    t.forward(20)
    sleep(0.1)
    info_choice = turtle.textinput('.', 'Choose level about you want info')
    t.forward(20)
    clean()
    t.goto(-500,340)
    if info_choice == "easy-info":
        sleep(0.5)
        t.forward(20)
        t.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        t.forward(20)
        easy_info()
        t.forward(20)
        t.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        t.forward(20)
        info()
        t.forward(20)
    elif info_choice == "medium-info":
        sleep(0.5)
        t.forward(20)
        t.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        t.forward(20)
        medium_info()
        t.forward(20)
        t.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        t.forward(20)
        info()
    elif info_choice == "hard-info":
        sleep(0.5)
        t.forward(20)
        t.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        t.forward(20)
        hard_info()
        t.forward(20)
        t.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        t.forward(20)
        info()
    elif info_choice == "impo-info":
        sleep(0.5)
        t.forward(20)
        t.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        t.forward(20)
        impo_info()
        t.forward(20)
        t.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        t.forward(20)
        info()
    elif info_choice == "return":
        
        sleep(0.5)
        t.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        t.forward(20)
        dif_levels() 


def dif_levels():
    t.goto(-500,340)
    t.color('white')
    t.write("Choose the difficulty level", font = ("Arial",15, 'bold'))
    t.forward(20)
    sleep(0.1)
    t.write("____________________________________", font = ("Arial", 10, ))
    t.forward(20)
    sleep(0.1)
    t.color('green')
    t.left(90)
    t.write("| Easy |", font = ("Arial", 10, 'bold'))
    t.forward(50)
    t.color('yellow')
    t.write(" Medium |", font = ("Arial", 10, 'bold' ))
    t.forward(60)
    sleep(0.1)
    t.color('orange')
    t.write("| Hard |", font = ("Arial", 10, 'bold' ))
    t.forward(50)
    t.color('red')
    t.write("| Imposible |", font = ("Arial", 10, 'bold' ))
    t.right(90)
    t.color('white')
    t.forward(30)
    t.write("------------------------------------", font = ("Arial", 10, ))
    t.forward(20)
    sleep(0.5)
    t.write("Type easy if you want to play on easy mode", font = ("Arial", 10, ))
    t.forward(20)
    sleep(0.1)
    t.write("Type medium if you want to play on medium mode", font = ("Arial", 10, ))
    t.forward(20)
    sleep(0.1)
    t.write("Type hard if you want to play on hard mode", font = ("Arial", 10, ))
    t.forward(20)
    sleep(0.1)
    t.write("Type impo if you want to play on imposible mode", font = ("Arial", 10, ))
    t.forward(20)
    sleep(0.1)
    t.write("_________________________________________________", font = ("Arial", 10, ))
    t.forward(20)
    sleep(0.1)
    t.write("Type info if you want to get mor information about difficulty levels", font = ("Arial", 10, ))
    t.forward(20)
    mode_chose = turtle.textinput('.', 'Choose difficulty level.')
    clean()
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
        t.write("Something went wrong")
       
def game_start():     
    t.goto(-500,340)
    t.right(90)
    t.color('blue')
    t.write("")
    t.forward(15)
    sleep(0.1)
    t.write('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄', font = ("Arial", 12, ))
    t.forward(25)
    sleep(0.1)
    t.write('█─▄▄▄▄█▄─██─▄█▄─▄▄─█─▄▄▄▄█─▄▄▄▄███▄─▀█▄─▄█▄─██─▄█▄─▀█▀─▄█▄─▄─▀█▄─▄▄─█▄─▄▄▀█', font = ("Arial", 12, ))
    t.forward(25)
    sleep(0.1)
    t.write('█─██▄─██─██─███─▄█▀█▄▄▄▄─█▄▄▄▄─████─█▄▀─███─██─███─█▄█─███─▄─▀██─▄█▀██─▄─▄█', font = ("Arial", 12, ))
    t.forward(25)
    sleep(0.1)
    t.write('█▄▄▄▄▄██▄▄▄▄██▄▄▄▄▄█▄▄▄▄▄█▄▄▄▄▄███▄▄▄██▄▄██▄▄▄▄██▄▄▄█▄▄▄█▄▄▄▄██▄▄▄▄▄█▄▄█▄▄█', font = ("Arial", 12, ))
    t.forward(25)
    sleep(0.3)
    t.color('green')
    t.write('                        ███████████████████████████                        ', font = ("Arial", 12, ))
    t.forward(25)
    sleep(0.2)
    t.write('                        █─▄▄▄▄██▀▄─██▄─▀█▀─▄█▄─▄▄─█                        ', font = ("Arial", 12, ))
    t.forward(25)
    sleep(0.2)
    t.write('                        █─██▄─██─▀─███─█▄█─███─▄█▀█                        ', font = ("Arial", 12, ))
    t.forward(25)
    sleep(0.2)
    t.write('                        █▄▄▄▄▄█▄▄█▄▄█▄▄▄█▄▄▄█▄▄▄▄▄█                        ', font = ("Arial", 12, ))
    t.forward(25)
    sleep(0.4)
    t.write('                                                                           ', font = ("Arial", 12, ))
    t.forward(25)
    t.write('                                                                           ', font = ("Arial", 12, ))
    t.forward(40)
    t.color("white")
    t.write('                       TYPE START TO START THE GAME                        ', font = ("Arial", 10, ))
    t.forward(15)
    start_choice = turtle.textinput('.', 'Do you want to start a game? If so type START.')
    if start_choice == "START" or "start" or "Start":
        sleep(0.5)
        clean()

        dif_levels()

game_start()


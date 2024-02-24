##imports graphics and random library
from graphics import *
import random

print("welcome to hangman")

#creates the gallow
def gallow():
    gallow = Rectangle(Point(180, 20), Point(320, 220))
    gallow.draw(mainwindow)
    gallow.setWidth(2)
    gallow.setOutline("White")
##the following functions all create the stick figure
def head():
    head = Circle(Point(250, 70), 20)
    head.draw(mainwindow)
    head.setWidth(5)
    head.setFill("white")

def body():
    body = Line(Point(250, 90), Point(250, 155))
    body.draw(mainwindow)
    body.setWidth(5) 
    body.setFill("white")

def leftarm():
    leftarm = Line(Point(250, 90), Point(200, 125))
    leftarm.draw(mainwindow)
    leftarm.setWidth(5) 
    leftarm.setFill("white")

def rightarm():
    rightarm = Line(Point(250, 90), Point(300, 125))
    rightarm.draw(mainwindow)
    rightarm.setWidth(5)
    rightarm.setFill("white")

def leftleg():
    leftleg = Line(Point(250, 155), Point(200, 200))
    leftleg.draw(mainwindow)
    leftleg.setWidth(5)
    leftleg.setFill("white")

def rightleg():
    rightleg = Line(Point(250, 155), Point(300, 200))
    rightleg.draw(mainwindow)
    rightleg.setWidth(5)
    rightleg.setFill("white")


#creates the main screen

mainwindow = GraphWin("Main Screen", 500, 500)
mainwindow.setBackground("black")
#creates the title text "Hangman!"
titletext = Text(Point(250, 100), "HANGMAN!")
titletext.setFace("courier")
titletext.setTextColor("white")
titletext.setSize(20)
titletext.draw(mainwindow)
    

 #creates a button
play_button = Rectangle(Point(175, 300), Point(325, 350))
play_button.setFill("green")
play_button.draw(mainwindow)

#creates main image
img = Image(Point(250,200), "hangmanimage.png")
img.draw(mainwindow)

#adds label to the button
button_text = Text(play_button.getCenter(), "PLAY")
button_text.setFace("courier")
button_text.setTextColor("white")
button_text.draw(mainwindow)

##list of words taken from a list online
wordlist = ["abruptly", "haiku", "absurd", "abyss", "affix","quiz","haphazard","banjo","bayou","bikini","subway","jinx","swivel","syndrome","spritz","jumbo","cobweb","crypt","croquet","cycle","boxful","daiquiri","klutz","vixen","khaki","microwave","mnemonic","wave","waltz","transcript","pixel","polka","yummy","galaxy","gazebo","whiskey","irish","zigzag"]


 
#allows button to be clicked to begin the game
while True:
    click = mainwindow.getMouse()
    if play_button.getP1().getX() <= click.getX() <= play_button.getP2().getX() and \
    play_button.getP1().getY() <= click.getY() <= play_button.getP2().getY():
        play_button.undraw()
        button_text.undraw()
        img.undraw()
        titletext.undraw()
        gallow()
        break

incorrect_guesses = 0


word = random.choice(wordlist)
word = word.upper()
word_letters = set(word) #keeps track of correct letters in word
guessed_letters = set() #keeps track of letters the user has guessed
print(word_letters)
print(word)

#creates the submit button
submit_button = Rectangle(Point(400, 300), Point(450, 350))
submit_button.setFill("Green")
submit_button.draw(mainwindow)

#creates the exitbutton
exit_button = Rectangle(Point(400, 200), Point(450, 250))
exit_button.setFill("Red")
exit_button.draw(mainwindow)

#creates the "exit" text
exit_submit = Text(exit_button.getCenter(), "exit")
exit_submit.setFace("courier")
exit_submit.setTextColor("white")
exit_submit.draw(mainwindow)


# creates the "submit" text
text_submit = Text(submit_button.getCenter(), "Submit")
text_submit.setFace("courier")
text_submit.setTextColor("white")
text_submit.draw(mainwindow)

## creates input boxes 
input_box = Entry(Point(250, 300), 10)
input_box.setFill("white")
input_box.draw(mainwindow)

## creates the dashed line that appears on screen according to the randomly generated word.
display_word = ["_"] * len(word)
display_text = Text(Point(250, 250), " ".join(display_word))
display_text.setSize(20)
display_text.setFill("white")
display_text.draw(mainwindow)

##main while loop that keeps the game going until the user loses.
while incorrect_guesses < 6:
    while True:
        #When the submit_button is clicked, the user's guess is stored in the "guess" variable
        buttonclick = mainwindow.getMouse()
        if submit_button.getP1().getX() <= buttonclick.getX() <= submit_button.getP2().getX() and \
        submit_button.getP1().getY() <= buttonclick.getY() <= submit_button.getP2().getY():
            guess = input_box.getText()
            guess = guess.upper()
            guessed_letters.add(guess)
            print(guess)
        #Exit_button allows the player to exit the program.
        if exit_button.getP1().getX() <= buttonclick.getX() <= exit_button.getP2().getX() and \
        exit_button.getP1().getY() <= buttonclick.getY() <= exit_button.getP2().getY():
            mainwindow.close()
        break

    while incorrect_guesses < 6: 
        
        if guess in word_letters:
            # if the guess is in the set, then this for loop is activated that checks which letters in the word the user guessed correctly
            # and updates the screen appropriately
            for i in range(len(word)):
                if word[i] == guess:
                    display_word[i] = guess
            display_text.setText(" ".join(display_word))
            ## prompts the player that they won after all the dashes are no longer in "display_word"
            if "_" not in display_word:
                wintext = Text(Point(250, 400), "You won!")
                wintext.setFace("courier")
                wintext.setTextColor("white")
                wintext.setSize(20)
                wintext.draw(mainwindow)
        ## counts the incorrect guesses and creates the stick figure     
        if guess not in word_letters:
         
            incorrect_guesses += 1
            if incorrect_guesses == 1:
                head()    
            if incorrect_guesses == 2:
                body()
            if incorrect_guesses == 3:
                leftarm()
            if incorrect_guesses == 4:
                rightarm()
            if incorrect_guesses == 5:
                leftleg()
            if incorrect_guesses == 6:
                rightleg()
                ##Creates text that tells user that they lost and what the answer was.
                repeatedtext = Text(Point(250, 400), "You lost! It was " + word + ".")
                repeatedtext.setFace("courier")
                repeatedtext.setTextColor("white")
                repeatedtext.setSize(20)
                repeatedtext.draw(mainwindow)

        break
mainwindow.getMouse()
mainwindow.close()

    
    









  




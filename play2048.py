#Lam Le

#TODO: Import the module that will allow you to use Selenium
from selenium import webdriver
#TODO: Import the module that will allow you to use the up, down, left, and right keys on your keyboard
from selenium.webdriver.common.keys import Keys

def play2048( times ):
    #TODO: write code in this function that:
    # 1. opens a game of 2048 from the URL: https://gabrielecirulli.github.io/2048/
    # 2. uses the parameter 'times' to determine how many times your code will try to play the game
    # 3. for each 'time', press these keys in this order: UP, RIGHT, DOWN, LEFT
    # 4. print the final score after all tries to the screen 

    browser = webdriver.Firefox() #opens up the game from firefox
    browser.open('https://gabrielecirulli.github.io/2048/') #this opens a game of 2048 from the URL

    htmltagElem = webbrowser.find_element_by_tag_name('html') #finds all the elements with matching tag name
    scoreElem = browser.find_element_by_class_name('score-container') #elements that use the CSS class name

    moves = 0 #moves equal zero

    while moves < times: #while moves is lesser than time
        htmlElem.send_keys(Keys.UP) #Makes the keys go UP
        htmlElem.send_keys(Keys.RIGHT) #Makes the keys go RIGHT
        htmlElem.send_keys(Keys.DOWN) #Makes the keys go DOWN
        htmlElem.send_keys(Keys.LEFT) #Makes the keys go LEFT

        moves += 1 #Moves plus equal one
 
    print('Your final score is: ' +scoreElem.text) #Lets the user know what their final score is

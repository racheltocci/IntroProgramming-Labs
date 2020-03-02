colors =["RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "INDIGO", "VIOLET", "BLACK", "WHITE", "BROWN"]

def showTitle():

    print("Color Preference Evaluator")
    
def promptforColor():

    color = input("Enter a color: ")

    color = color.upper()

    color = color.strip()

    return color

def confirmColor(color):

    while (1==1):

        yesno = input("You entered " + color + ". Is this correct? (Y/N)")

        if (yesno.lower() == "y"):
            return True
        elif (yesno.lower() == "n"):
            return False
        else:
            print("Invalid input.")

def containsElements(color):
    for x in colors:
        if (color == x):
            return True
    return False

def praiseUser():
    print("Good job that color is valid!")
    
def ridiculeUser():
    print("Oh no! That color is invalid!")
    
def main():
    showTitle()
    color = promptforColor()
    ratatat = 0
    while (confirmColor(color) != True):
        color = promptforColor()
        color = color.upper()
    if (containsElements(color)==True):
        praiseUser()
    else:
        ridiculeUser()
main()

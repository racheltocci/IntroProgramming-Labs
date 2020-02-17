def main():
    title = "Welcome to the Python Guessing Game by Rachel"
    print(title)
    animal = "panda"
    zero = 0
    while zero == 0:
        guess = input ("Guess the animal I am thinking of: ")
        if guess == animal:
            zero += 1
            print("Congratulations you guessed the animal!")
        else:
            print("Wrong animal, try again.")        
main()

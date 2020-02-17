def main():
    title = "Welcome to the Python Guessing Game by Rachel"
    print(title)
    animal = "panda"
    zero = 0
    while zero == 0:
        guess = input ("Guess the animal I am thinking of: ")
        if guess.lower() == animal:
            zero += 1
            print("Congratulations you guessed the animal!")
            Thepanda = 0
            while Thepanda == 0: 
                response = input("Do you like this animal? Y/N: ")
                if response[0].lower() == "n":
                    print("Aw that's a shame they're so cute.")
                    Thepanda += 1
                elif response [0].lower() == "y":
                    print("Yay me too!")
                    Thepanda += 1
        elif guess[0].lower() == "q":
            zero += 1
        else:
            print("Wrong animal, try again.")
    print("Thanks for playing.")
main()

# created a function to create a number guessing game
def number_guessing_game_created():
    print("Welcome To The Number Guessing Game!")
    print("Guess a number between 1 & 100")

    # Function to generate a unique number
    def generate_unique_number():
        now = str(time.time())  # get current time in seconds
        # Use the last 5 digits of the current time to create a unique number
        digits = now.replace('.', '')[-5:]
        return int(digits) % 100  # returns a number from 0 to 99

    import time
    # storing the generated number in a variable
    secret_number = generate_unique_number()
    print("Generated:", secret_number)

    # initializing the number of attempts
    attempts = 0

    while attempts < 5:
        try:
            # Taking input from the user
            guess = int(input("Your Guess: "))
        except ValueError:
            print("Please enter a valid integer!")
            continue

        if guess < secret_number:
            print("Too Low!")
        elif guess > secret_number:
            print("Too High!")
        else:
            print("The secret number is correct", guess)
            break

        # Incrementing the number of attempts
        attempts += 1

    if attempts == 5:
        print("You have used all your attempts. The secret number was:", secret_number)

    # Offer a rematch
    rematch = input("Do you want to play again? (yes/no): ")
    if rematch.lower() == "yes":
        number_guessing_game_created()
    else:
        print("Thank you for playing!")

# Call the function to start the game
number_guessing_game_created()

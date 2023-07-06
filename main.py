import random

# List of music genres
genres = ['pop', 'rock', 'hip hop', 'country', 'jazz', 'electronic']

# Select a random genre
random_genre = random.choice(genres)

# Display instructions to the user
print("Guess the music genre!")

# Variable to track number of attempts
attempts = 0

# Loop until the user guesses correctly
while True:
    # Get user input
    guess = input("Enter your guess: ")

    # Increment number of attempts
    attempts += 1

    # Check if user's guess is correct
    if guess.lower() == random_genre:
        print("Congratulations! You guessed it right.")
        break
    else:
        print("Wrong guess! Try again.")

# Display number of attempts
print("Number of attempts:", attempts)
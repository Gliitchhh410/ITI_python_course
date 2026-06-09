import random

def play_guessing_game():
    print("The system will generate a number between 1 and 100.")
    
    target_number = random.randint(1, 100)
    max_tries = 10
    tries_used = 0
    guessed_numbers = set()

    while tries_used < max_tries:
        remaining_tries = max_tries - tries_used
        print(f"\nYou have {remaining_tries} tries left.")
        
        user_input = input("Enter your guess (1-100): ")
        
        if not user_input.isdigit():
            print("Invalid input. Please enter a positive integer.")
            continue
            
        guess = int(user_input)

        if guess < 1 or guess > 100:
            print("Out of range! Number must be between 1 and 100. This try won't count.")
            continue

        if guess in guessed_numbers:
            print("You already guessed that number! Try a different one. This try won't count.")
            continue

        guessed_numbers.add(guess)
        tries_used += 1

        if guess == target_number:
            print(f"Congratulations! You guessed the correct number: {target_number}")
            
            if tries_used < max_tries:
                print("Generating a new random number for your remaining tries...")
                target_number = random.randint(1, 100)
                guessed_numbers.clear() 
            else:
                break
        elif guess < target_number:
            print("Hint: Your guess is smaller than the target number.")
        else:
            print("Hint: Your guess is bigger than the target number.")

    if tries_used >= max_tries:
        print("\nGame Over! You have run out of tries.")
    
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again in ('yes', 'y'):
        play_guessing_game()
    else:
        print("Thanks for playing!")

play_guessing_game()
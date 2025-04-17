import random

def main():
    print("Welcome to the Guessing Game 😃 !!!")
    mode = select_level()
    guess_number(mode)

def select_level() -> dict:
    game_modes = [
        {"level": "easy", "num_attempts": 15, "num_range": [1, 30]},
        {"level": "medium", "num_attempts": 10, "num_range": [1, 50]},
        {"level": "hard", "num_attempts": 5, "num_range": [1, 100]}
    ]
    levels = [mode["level"] for mode in game_modes]
    
    while True:
        select_mode = input("Select a mode: Easy, Medium, or Hard: ").lower()
        if select_mode not in levels:
            print("Please select either: Easy, Medium, or Hard")
        else:
            return next(mode for mode in game_modes if mode["level"] == select_mode)

def get_random_number(first, last) -> int:
    random_number = random.randint(first, last)
    return random_number

def guess_number(mode: dict):
    print(f"Rule 📝: You have only {mode["num_attempts"]} attempts")
    attempt = 0
    random_number = get_random_number(mode["num_range"][0], mode["num_range"][1])
    
    while True:
        user_choice = int(input(f"Pick a number between {mode["num_range"][0]} and {mode["num_range"][1]}: "))
        attempt += 1
        if (user_choice > random_number) and (attempt < mode["num_attempts"]):
            print("Too High ⬆️!")
        elif (user_choice < random_number) and (attempt < mode["num_attempts"]):
            print("Too Low ⬇️!")
        else:
            if (attempt == mode["num_attempts"]) and (user_choice != random_number):
                print("You've run out of attempts 😔")
            else:
                print("You Got It 🥳 !!!")
            break

if __name__ == "__main__":
    main()

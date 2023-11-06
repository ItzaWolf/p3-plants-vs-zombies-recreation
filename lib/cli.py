# lib/cli.py

from helpers import (
    exit_program,
    helper_1
)

user_data = {}

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            print("The game is currently being made! Not ready yet!")
            helper_1()
        elif choice == "2":
            sign_up()
        elif choice == "3":
            sign_in()
        elif choice == "4":
            high_scores()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Start Game")
    print("2. Get Started & Sign up")
    print("3. Sign In")
    print("4. High Scores")

def sign_up():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    
    if username in user_data:
        print("Username already exists. Please choose a different username.")
    else:
        user_data[username] = password
        print("Account created successfully!")


def sign_in():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username in user_data and user_data[username] == password:
        print(f"Login successful. Welcome,{username}!")
        # Add code to continue the game or perform other actions here
    else:
        print("Invalid username or password. Please try again.")


def high_scores():
    # Add code to display high scores
    print("High Scores")


if __name__ == "__main__":
    main()

import warnings
from sqlalchemy import exc as sa_exc
warnings.filterwarnings("ignore", category=sa_exc.MovedIn20Warning)
from game import init_game, run_game, quit_game
from helpers import exit_program, helper_1
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///pvz.db")
Session = Session(engine)
user_data = {}
user_logged_in = False

class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key= True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

class Scores(Base):
    __tablename__ = "Scores"
    id = Column(Integer, primary_key= True)
    user_id = Column(Integer, ForeignKey("Users.id"))
    score = Column(Integer, nullable=False)

def main():
    global user_logged_in

    while True:
        menu(user_logged_in)
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            start_game()
        elif choice == "2":
            high_scores()
        elif choice == "3":
            if user_logged_in == False:
                sign_up()
            elif user_logged_in == True:
                update_info()
        elif choice == "4":
            if user_logged_in == False:
                sign_in()
            elif user_logged_in == True:
                delete_info()
        else:
            print("Invalid choice")

def menu(user_logged_in):
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Start Game")
    print("2. High Scores")
    if user_logged_in == False:
        print("3. Get Started & Sign up")
        print("4. Sign In")
    if user_logged_in == True:
        print("3. Update Account Information")
        print("4. Delete Account")

def sign_up():
    global user_logged_in

    username = input("Enter a username: ")
    password = input("Enter a password: ")

    existing_user = Session.query(Users).filter(Users.username == username).first()
    if existing_user:
        print("Username already exists. Please choose a different username.")
    else:
        new_user = Users(username=username, password=password)
        Session.add(new_user)
        Session.commit()
        user_logged_in = True
        print("Account created successfully!")

def sign_in():
    global user_logged_in

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    user = Session.query(Users).filter(Users.username == username, Users.password == password).first()
    if user:
        print(f"Login successful. Welcome, {user.username}!")
        user_logged_in = True
        return user
    else:
        print("Invalid username or password. Please try again.")
        return None

def update_info():
    global user_logged_in

    print("Update Account Information")
    print("1. Change Password")
    print("2. Change Username")
    print("3. Go back to the main menu")
    
    choice = input("> ")

    if choice == "1":
        change_password()
    elif choice == "2":
        change_username()
    elif choice == "3":
        return
    else:
        print("Invalid choice")

def change_password():
    username = input("Enter your username: ")
    old_password = input("Enter your current password: ")
    
    user = Session.query(Users).filter(Users.username == username, Users.password == old_password).first()
    if user:
        new_password = input("Enter your new password: ")
        user.password = new_password
        Session.commit()
        print("Password updated successfully!")
    else:
        print("Invalid username or password. Password update failed.")

def change_username():
    global user_logged_in

    username = input("Enter your current username: ")
    password = input("Enter your password: ")

    user = Session.query(Users).filter(Users.username == username, Users.password == password).first()
    if user:
        new_username = input("Enter your new username: ")

        existing_user = Session.query(Users).filter(Users.username == new_username).first()
        if existing_user:
            print("Username already exists. Please choose a different username.")
        else:
            user.username = new_username
            Session.commit()
            print("Username updated successfully!")
            user_logged_in = False
    else:
        print("Invalid username or password. Username update failed.")

def delete_info():
    global user_logged_in

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    user = Session.query(Users).filter(Users.username == username, Users.password == password).first()
    if user:
        confirmation = input("This will wipe all current user data, including your unlocks, high scores, and game progress. Are you sure you want to delete your account? (yes/no): ")
        if confirmation.lower() == "yes":
            Session.delete(user)
            Session.commit()
            user_logged_in = False
            print("Account deleted successfully! Sorry to see you go! :(")
        else:
            print("Account deletion canceled.")
    else:
        print("Invalid username or password. Account deletion canceled.")

def start_game():
    init_game()
    run_game()
    quit_game()

def high_scores():
    print("High Scores")

if __name__ == "__main__":
    main()
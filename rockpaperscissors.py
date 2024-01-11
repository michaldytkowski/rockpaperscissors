import random

def versus(x, y):
    if x == "rock":
        if y == "paper":
            print(f"{x} VS {y}! {y} is a winner!")
        elif y == "scissors":
            print(f"{x} VS {y}! {x} is a winner!")
        elif y == "scissors":
            print(f"{x} VS {y}! Its a tie!")
    elif x == "paper":
        if y == "rock":
            print(f"{x} VS {y}! {x} is a winner!")
        elif y == "scissors":
            print(f"{x} VS {y}! {y} is a winner!")
        elif y == "scissors":
            print(f"{x} VS {y}! Its a tie!")
    elif x == "scissors":
        if y == "rock":
            print(f"{x} VS {y}! {y} is a winner!")
        elif y == "paper":
            print(f"{x} VS {y}! {x} is a winner!")
        elif y == "scissors":
            print(f"{x} VS {y}! Its a tie!")


x = input("Your choice (rock, paper or scissors): ")
y = random.choice(["rock", "paper", "scissors"])
#print(y)
versus(x, y)

from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if play == "y":
    print(logo)
    for n in range(0, 1):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))

    print(f"Your cards: {user_cards}, current score: {user_cards[0] + user_cards[1]}")
    print(f"Computer's first card: {computer_cards[0]}")
    input("Do you want to play a game of Blackjack? Type 'y' or 'n':")


from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while play == "y":
    user_cards = []
    computer_cards = []
    print(logo)

    for n in range(0, 2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))

    if sum(computer_cards) == 21:
        print(f"Computer win: {computer_cards}")
    elif sum(user_cards) == 21:
        print(f"You win: {user_cards}")
    else:
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")

        # USER TURN
        user_more_card = "y"
        while user_more_card == "y":
            user_more_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_more_card == "y":
                user_cards.append(random.choice(cards))
                # check if user score is more than 21 and if includes aces
                if sum(user_cards) > 21:
                    for n in range(0, len(user_cards)):
                        if user_cards[n] == 11:
                            user_cards[n] = 1
                    print(f"User cards TEST: {user_cards}")
                    if sum(user_cards) > 21:
                        user_more_card = "n"
                if not sum(user_cards) > 21:
                    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
                    print(f"Computer's first card: {computer_cards[0]}")
        # COMPUTER TURN
        while sum(computer_cards) <= 16:
            computer_cards.append(random.choice(cards))
            # check if computer score is more than 21 and if includes aces
            if sum(computer_cards) > 21:
                for n in range(0, len(computer_cards)):
                    if computer_cards[n] == 11:
                        computer_cards[n] = 1
                print(f"Computer cards TEST: {computer_cards}")

        # User and Computer compare
        print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
        print(f"Computer final hand: {computer_cards}, final score: {sum(computer_cards)}")

        if sum(user_cards) > 21:
            print("You went over. You loose")
        elif sum(computer_cards) > 21:
            print("Opponent went over. You win 😁")
        else:
            if sum(computer_cards) > sum(user_cards):
                print("Opponent has higher score. You loose")
            elif sum(computer_cards) < sum(user_cards):
                print("You have higher score. You win 😁")
            else:
                print("It's a draw")

    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

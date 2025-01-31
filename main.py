from art import logo
import random

def start_question():
    while True:
        user_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n'\n").lower()
        if user_playing == "y":
            return True
        elif user_playing == "n":
            return False
        else:
            print("Invalid input, please type 'y' or 'n'")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while start_question():
    # Clear the screen & display logo
    print("\n" * 20)
    print(logo)

    # Users First Cards
    user_cards = random.sample(cards, 2)
    users_total = sum(user_cards)
    print(f"You cards are: {user_cards}, current score: {users_total}")


    # Computers First Card
    computers_card = random.sample(cards, 2)
    computers_total = sum(computers_card)
    print(f"Computers first card: {computers_card[0]}")


    # IF DRAW OFF FIRST 2 CARDS
    if computers_total == 21 and users_total == 21:
        print(f"DRAW! No one wins... Computer drew: {computers_card[0]} and {computers_card[1]}. Totalling {computers_total}")
        continue

    # IF COMPUTER WINS OFF FIRST 2 CARDS
    if computers_total == 21 and users_total < 21:
        print(f"GAME OVER! Computer drew: {computers_card[0]} and {computers_card[1]}. Totalling {computers_total}")
        continue

    # IF USER WINS OFF FIRST 2 CARDS
    if users_total == 21 and computers_total < 21:
        print(f"GAME OVER, YOU WIN! BLACKJACK YOUR TOTAL IS {users_total}")
        continue

    # PLAYERS NEXT GO
    while users_total < 21:
        another_card = input("Type 'y' to get another card, type 'n' to pass:").lower()
        if another_card == "y":
            new_card = random.sample(cards, 1)[0]
            user_cards.append(new_card)
            users_total = sum(user_cards)
            print(f"Your cards: {user_cards}, current score: {users_total}")

            # Check if player hits exactly 21
            if users_total == 21:
                print("You hit 21! You win!")
                break
            # Checks if player busts
            if users_total > 21:
                print("You went over 21! You lose.")
                break
        elif another_card == "n":
            break
        else:
            print("Invalid input. Please type 'y' or 'n'")

    # COMPUTERS NEXT GO
    if users_total < 21:  # player didn't bust
        print(f"Computer's cards: {computers_card}, current score: {computers_total}")
        while computers_total < 17:
            new_card = random.sample(cards, 1)[0]
            computers_card.append(new_card)
            computers_total = sum(computers_card)
            print(f"Computer drew a card: {new_card}. Current score: {computers_total}")

        # WIN CONDITIONS
        if computers_total > 21:
            print("The computer went over 21! You win!")
        elif computers_total > users_total:
            print("You Lose!")
        elif computers_total < users_total:
            print("You Win!")
        else:
            print("It's a draw!")














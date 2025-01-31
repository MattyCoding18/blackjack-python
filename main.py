from art import logo
import random

def start_question():
    """Asks user if they want to play Blackjack, returns True if yes, False if no"""
    while True:
        user_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n'\n").lower()
        if user_playing in ["y", "n"]:
            return user_playing == "y"
        print("Invalid input, please type 'y' or 'n'")

def calculate_total(cards):
    """
    Calculates the total score of a given hand.
    Adjusts Ace (11 -> 1) if total exceeds 21.
    """
    total = sum(cards)
    while total > 21 and 11 in cards:
        cards[cards.index(11)] = 1  # Convert first Ace from 11 to 1
        total = sum(cards)
    return total

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while start_question():
    # Clear the screen & display logo
    print("\n" * 20)
    print(logo)

    # Player's initial hand
    user_cards = random.sample(cards, 2)
    users_total = calculate_total(user_cards)
    print(f"Your cards are: {user_cards}, current score: {users_total}")

    # Computer's initial hand
    computers_card = random.sample(cards, 2)
    computers_total = calculate_total(computers_card)
    print(f"Computer's first card: {computers_card[0]}")

    # Immediate win/loss conditions
    if users_total == 21 and computers_total == 21:
        print(f"DRAW! Both have Blackjack. Computer had {computers_card}.")
        continue
    elif computers_total == 21:
        print(f"GAME OVER! Computer has Blackjack with {computers_card}.")
        continue
    elif users_total == 21:
        print(f"CONGRATULATIONS! You got a Blackjack with {user_cards}!")
        continue

    # Player's turn
    while users_total < 21:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if another_card == "y":
            user_cards.append(random.choice(cards))
            users_total = calculate_total(user_cards)
            print(f"Your cards: {user_cards}, current score: {users_total}")
        elif another_card == "n":
            break
        else:
            print("Invalid input. Please type 'y' or 'n'.")

    # Player busts
    if users_total > 21:
        print("You went over 21! You lose.")
        continue

    # Computer's turn
    print(f"Computer's cards: {computers_card}, current score: {computers_total}")
    while computers_total < 17:
        new_card = random.choice(cards)
        computers_card.append(new_card)
        computers_total = calculate_total(computers_card)
        print(f"Computer drew a card: {new_card}. Current score: {computers_total}")

    # Final result
    if computers_total > 21:
        print("The computer went over 21! You win!")
    elif computers_total > users_total:
        print("You Lose!")
    elif computers_total < users_total:
        print("You Win!")
    else:
        print("It's a draw!")

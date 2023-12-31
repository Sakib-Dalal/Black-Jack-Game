import random
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "The game is Draw 🙃"
    elif computer_score == 0:
        return "You Lose The Game 😭"
    elif user_score > 21:
        return "You Lose The Game 😭"
    elif user_score == 0:
        return "You Win The Game 🥳"
    elif computer_score > 21:
        return "You Win The Game 🥳"
    elif user_score > computer_score:
        return "You Win The Game 🥳"
    else:
        return "You Lose The Game 😭"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print()
        print(f"    Your cards {user_cards}, current score: {user_score}")
        print(f"    Computers first card {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            print()
            user_should_deal = input("Type 'y' to get another card, or 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your score is: {user_score}, computer score is: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play game of Blackjack, type 'y' to play, or 'n' to no: ").lower() == 'y':
    play_game()

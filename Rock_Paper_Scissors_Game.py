import random
print("===== Rock, Paper, Scissors Game =====")

def get_user_choice():
    print("\nChoose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Enter 1, 2 or 3: ")

    if choice == '1':
        return 'rock'
    elif choice == '2':
        return 'paper'
    elif choice == '3':
        return 'scissors'
    else:
        print("Invalid input. Try again.")
        return get_user_choice()

def get_computer_choice():
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)

def check_winner(player, computer):
    if player == computer:
        return 'draw'
    elif player == 'rock' and computer == 'scissors':
        return 'player'
    elif player == 'paper' and computer == 'rock':
        return 'player'
    elif player == 'scissors' and computer == 'paper':
        return 'player'
    else:
        return 'computer'

def main():
    user_score = 0
    comp_score = 0

    while True:
        user = get_user_choice()
        comp = get_computer_choice()

        print("\nYou selected:", user)
        print("Computer selected:", comp)

        result = check_winner(user, comp)

        if result == 'draw':
            print("Match is draw.")
        elif result == 'player':
            print("You got this round!")
            user_score = user_score + 1
        else:
            print("Computer won this round.")
            comp_score = comp_score + 1

        print("Current Score:")
        print("You =", user_score)
        print("Computer =", comp_score)

        again = input("\nWant to play again? (y/n): ")
        if again == 'n' or again == 'N':
            print("\nGame Over.")
            print("Final Score:")
            print("You =", user_score)
            print("Computer =", comp_score)
            print("Thanks for playing :)")
            break
        
main()

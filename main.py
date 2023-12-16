import random

should_continue = True
while should_continue:
    print("\nWelcome to Rock/Scissors/Paper game!")
    rsp = ["rock", "scissors", "paper"]
    computer_choice = random.choice(rsp)
    player_choice = input("What do you chose ? Rock/Scissors/Paper : ").lower()
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    elif player_choice == "paper" and computer_choice == "rock":(
        print("You win!"))
    elif player_choice == "stop":
        should_continue = False
        print("Goodbye!")
    else:
        print("You lose!")
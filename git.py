def rock_paper_scissors(player1, player2):
    # Normalize inputs to lowercase
    p1 = player1.lower()
    p2 = player2.lower()

    # Check for a tie
    if p1 == p2:
        return "It's a tie!"

    # Apply your custom winning rules
    if (p1 == "rock" and p2 in ["paper", "scissors"]) or (p1 == "paper" and p2 == "rock") or (p1 == "scissors" and p2 == "paper"):
        return "Player 1 wins!"
    elif (p2 == "rock" and p1 in ["paper", "scissors"]) or (p2 == "paper" and p1 == "rock") or (p2 == "scissors" and p1 == "paper"):
        return "Player 2 wins!"
    else:
        return "Invalid input! Please choose rock, paper, or scissors."

# Example usage
player1_input = input("Player 1 - Enter rock, paper, or scissors: ")
player2_input = input("Player 2 - Enter rock, paper, or scissors: ")

result = rock_paper_scissors(player1_input, player2_input)
print(result)

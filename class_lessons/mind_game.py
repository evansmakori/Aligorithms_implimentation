import random

def mind_match():
    print(" Welcome to Mind Match!")
    print("Can you guess what the computer picked?")
    print("Type your guess exactly as shown (case-sensitive).")
    print("Type 'quit' to end the game.\n")

    words_list = ["apple", "banana", "cherry", "grape", "orange", "kiwi", "mango", "lemon"]
    score = 0

    while True:
        # Pick 4 random words
        options = random.sample(words_list, 4)
        print("🔤 Here are your options:")
        for word in options:
            print(f"- {word}")

        # Computer picks one
        chosen = random.choice(options)

        # Get player's guess
        guess = input("\n🤔 Which word do you think the computer picked? ").strip()

        if guess.lower() == "quit":
            print("\n👋 Thanks for playing!")
            break

        if guess not in options:
            print("❌ That word wasn't one of the options. Try again.")
            continue

        # Check guess
        if guess == chosen:
            score += 1
            print("🎉 Correct! You earn 1 point.")
        else:
            print(f"😞 Wrong. The computer picked '{chosen}'.")

        print(f"🏅 Current Score: {score}\n")
        print("-" * 40)

    print(f"\n🏁 Final Score: {score} — See you next time!")

# Run the game
mind_match()

import random

def user_name():
    name = input("what is your name? ")
    return name

def choose_difficulty():
    while True:
        level = input("Choose a difficulty level(easy, medium, hard): ").lower()
        if level in ["easy","medium", "hard"]:
            return level
        else:
            print("Invalid input. Please enter 'easy', 'medium', or 'hard'.")

def generate_question(difficulty):
    if difficulty == "easy":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif difficulty == "medium":
        num1 = random.randint(10, 50)
        num2 = random.randint(10, 50)
    else: # hard
        num1 = random.randint(50, 100)
        num2 = random.randint(1, 100)

    operation = random.choice(["+", "-", "*", "/"])

    # Avoid division by zero and ensure clean division for simplicity
    if operation == "/":
        num1 = num1 * num2

    question = f"What is {num1} {operation} {num2}? "
    answer = eval(f"{num1} {operation} {num2}")
    return question, round(answer, 2)  # round for float division

def ask_questions(difficulty, num_questions=5):
    score = 0
    for i in range(num_questions):
            question, correct_answer = generate_question(difficulty)
            try: 
                user_answer = float(input(f"Q{i+1}: {question}"))
                if abs(user_answer - correct_answer) < 0.01:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Incorrect. :( The corret answer was {correct_answer}.")
            except ValueError:
                print("invalid input. Please enter a number. ")
    return score

def play_game():
    print("Welcome to the Math Quiz Game!")
    name = user_name()
    while True:
        level = choose_difficulty()
        score = ask_questions(level)
        print(f"{name}, your final score is {score}/5.")

        play_again = input("Do you want to play again?  (y/n): ").lower
        if play_again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
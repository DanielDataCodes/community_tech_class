def math_quiz()
    user_name = input("Hi, What is your name? ")
    diff_level = input(f"hi {user_name}. choose a difficulty level (easy, medium, hard) ")

    while True
        if diff_level.lower() not in ("easy", "medium", "hard")
            print("must be easy, medium or hard")
        else
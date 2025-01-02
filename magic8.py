def get_user_question():
    while True:
        question = input("Ask the Magic 8-Ball a question (or type 'exit' to quit): ")
        if question.strip().lower() == "exit":
            print("Goodbye!")
            return None

        elif question.strip() == "":
            print("Please ask a valid question!")
        else:
            return question
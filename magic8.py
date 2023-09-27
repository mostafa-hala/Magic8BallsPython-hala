import random

# Setup: name, question, and answer.
name = input("What is your name? \n")
question = input("Please ask your question \n")
answer = ""

# Generating random number.
random_number = random.randint(1, 20)

# Control flow
if random_number == 1:
    answer = "It is certain"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Yes, definitely"
elif random_number == 5:
    answer = "You may rely on it"
elif random_number == 6:
    answer = "As I see it, yes"
elif random_number == 7:
    answer = "Most likely"
elif random_number == 8:
    answer = "Outlook good"
elif random_number == 9:
    answer = "Yes"
elif random_number == 10:
    answer = "Reply hazy, try again"
elif random_number == 11:
    answer = "Ask again later"
elif random_number == 12:
    answer = "Better not tell you now"
elif random_number == 13:
    answer = "Cannot predict now"
elif random_number == 14:
    answer = "Concentrate and ask again"
elif random_number == 15:
    answer = "Don't count on it"
elif random_number == 16:
    answer = "My reply is no"
elif random_number == 17:
    answer = "My sources say no"
elif random_number == 18:
    answer = "Outlook not so good"
elif random_number == 19:
    answer = "Very doubtful"
else:
    answer = "Error"

# Print result.
if name == "":
    print("Question: " + question + "?")
    print("8 balls answer: " + answer)
elif question == "":
    print("Please state your question. Otherwise, 8 balls cannot answer.")
else:
    print(name + " asks: " + question + "?")
    print("8 balls answer: " + answer)


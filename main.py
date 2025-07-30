import random

def random_greeting():
    greetings = [
        "Hello, world!",
        "Hi there!",
        "Greetings!",
        "Howdy!",
        "Hey!",
        "Salutations!",
        "Good day!"
    ]
    return random.choice(greetings)

if __name__ == "__main__":
    print("Hello World")
    print(random_greeting())


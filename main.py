import random
from art import logo, vs
from data import data

print(logo)
option_a = option_b = []
score = 0

while option_a == option_b:
    option_a = random.choice(data)
    option_b = random.choice(data)


def game(option_a, option_b, score):
    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")
    print(vs)
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")

    if option_a['follower_count'] > option_b['follower_count']:
        answer = 'A'
    else:
        answer = 'B'

    guess = input(f"Who has more followers? Type 'A' or 'B': ")

    if guess == answer:
        score += 1
        print(f"You're right! Current score: {score}")
        option_a = option_b
        option_b = random.choice(data)
        game(option_a, option_b, score)
    else:
        print(f"Sorry, that's wrong. FInal score: {score}")


game(option_a, option_b, score)

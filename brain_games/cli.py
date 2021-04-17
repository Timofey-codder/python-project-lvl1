#!/usr/bin/env python3

import prompt
import random


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    return name


def game_numbers(name):
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    for number in range(3):
        question = random.randint(1, 99)

        if question % 2 == 0:
            true_answer = 'yes'
        else:
            true_answer = 'no'

        print("Question: ", question)
        answer = prompt.string('Your answer: ')

        if (question % 2 == 0 and answer == 'yes') or (question % 2 == 1 and answer == 'no'):
            print("Correct!")
        else:
            print("'" + answer + "' is wrong answer ;(. Correct answer was '" + true_answer + "'.")
            print("Let's try again, " + name + "!")
            return None

    print("Congratulations, " + name + "!")


def calc(name):
    print("What is the result of the expression?")
    symbol = random.randint(1,3)

    for number in range(3):
        print("Question:", end=" ")
        if symbol == 1:
            first = random.randint(1,99)
            second = random.randint(1,99)
            print(str(first) + " + " + str(second))
            result = first + second

        elif symbol == 2:
            first = random.randint(1,99)
            second = random.randint(1,99)

            while first < second:
                first = random.randint(1,99)
                second = random.randint(1,99)

            print(str(first) + " - " + str(second))
            result = first - second

        else:
            first = random.randint(1,99)
            second = random.randint(1,99)
            print(str(first) + " * " + str(second))
            result = first * second

        answer = prompt.string('Your answer: ')
        if str(result) == answer:
            print("Correct!")
        else:
            print("'" + answer + "' is wrong answer ;(. Correct answer was '" + str(result) + "'.")
            print("Let's try again, " + name + "!")
            return None

    print("Congratulations, " + name + "!")


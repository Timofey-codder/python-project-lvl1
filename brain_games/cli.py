#!/usr/bin/env python3

import prompt
import random
from math import gcd


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

        if (
            question % 2 == 0 and answer == 'yes') or (
                question % 2 == 1 and answer == 'no'):
            print("Correct!")
        else:
            print(
                "'" + answer + "' is wrong answer "
                ";(. Correct answer was '" + true_answer + "'.")
            print("Let's try again, " + name + "!")
            return None

    print("Congratulations, " + name + "!")


def calc(name):
    print("What is the result of the expression?")
    symbol = random.randint(1, 3)

    for number in range(3):
        print("Question:", end=" ")
        if symbol == 1:
            first = random.randint(1, 99)
            second = random.randint(1, 99)
            print(str(first) + " + " + str(second))
            result = first + second

        elif symbol == 2:
            first = random.randint(1, 99)
            second = random.randint(1, 99)

            while first < second:
                first = random.randint(1, 99)
                second = random.randint(1, 99)

            print(str(first) + " - " + str(second))
            result = first - second

        else:
            first = random.randint(1, 99)
            second = random.randint(1, 99)
            print(str(first) + " * " + str(second))
            result = first * second

        answer = prompt.string('Your answer: ')
        if str(result) == answer:
            print("Correct!")
        else:
            print(
                "'" + answer + "' is wrong answer ;(. "
                "Correct answer was '" + str(result) + "'.")
            print("Let's try again, " + name + "!")
            return None

    print("Congratulations, " + name + "!")


def gcd_calc(name):
    print("Find the greatest common divisor of given numbers.")

    for number in range(3):
        first = random.randint(1, 99)
        second = random.randint(1, 99)
        result = gcd(first, second)
        print("Question:", first, second)
        answer = prompt.string('Your answer: ')
        if str(result) == answer:
            print("Correct!")
        else:
            print(
                "'" + answer + "' is wrong answer ;(. "
                "Correct answer was '" + str(result) + "'.")
            print("Let's try again, " + name + "!")
            return None

    print("Congratulations, " + name + "!")


def progression(name):
    print("What number is missing in the progression?")

    ind = 0
    while ind < 3:
        count = random.randint(5, 10)
        differ = random.randint(1, 25)
        pos = random.randint(1, count) - 1
        first = random.randint(1, 99)
        print("Question: ", end='')

        for number in range(count):
            if number == pos:
                print("..", end=' ')
                result = first
            else:
                print(str(first), end=' ')

            first = first + differ

        print('')
        answer = prompt.string('Your answer: ')

        if str(result) == answer:
            print("Correct!")
        else:
            print(
                "'" + answer + "' is wrong answer ;(. "
                "Correct answer was '" + str(result) + "'.")
            print("Let's try again, " + name + "!")
            return None

        ind += 1

    print("Congratulations, " + name + "!")


def primer(name):
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")

    for number in range(3):
        count = random.randint(1, 99)
        print("Question:", count)
        answer = prompt.string('Your answer: ')

        if isPrime(count) is True:
            result = 'yes'
        else:
            result = 'no'

        if result == answer:
            print("Correct!")
        else:
            print(
                "'" + answer + "' is wrong answer ;(. "
                "Correct answer was '" + result + "'.")
            print("Let's try again, " + name + "!")
            return None

    print("Congratulations, " + name + "!")


def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

#!/usr/bin/env python3

from brain_games.cli import welcome_user, game_numbers


def main():
    name = welcome_user()
    game_numbers(name)


if __name__ == '__main__':
    main()
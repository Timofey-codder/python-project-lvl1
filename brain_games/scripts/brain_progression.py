#!/usr/bin/env python3

from brain_games.cli import welcome_user, progression


def main():
    name = welcome_user()
    progression(name)


if __name__ == '__main__':
    main()

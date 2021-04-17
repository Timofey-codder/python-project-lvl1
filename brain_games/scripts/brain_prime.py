#!/usr/bin/env python3

from brain_games.cli import welcome_user, primer


def main():
    name = welcome_user()
    primer(name)


if __name__ == '__main__':
    main()

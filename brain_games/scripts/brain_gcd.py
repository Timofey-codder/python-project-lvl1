#!/usr/bin/env python3

from brain_games.cli import welcome_user, gcd_calc


def main():
    name = welcome_user()
    gcd_calc(name)


if __name__ == '__main__':
    main()

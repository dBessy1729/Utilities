#!/bin/python3

import secrets
import string


ALPHABET = string.ascii_letters + string.digits
MAX = 8


def main():
    for i in range(MAX):
    	# where 8 is the number of passwords tp generate
    	password = ''.join(secrets.choice(ALPHABET) for i in range(32))
    	# where 32 is the character length of each password
    	print(password)


if __name__ == '__main__':
	main()

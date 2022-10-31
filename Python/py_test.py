#!/usr/bin/python
import os,sys,time

def tuple_fn():
	test_set = ((1,'a'), (2,'b'), (3,'c'))

	for t in test_set:
		print t

	for num, alph in test_set:
		print num, alph 

def list_fn():
	test_list = [[1,'a'], [2,'b'], [3,'c']]

	for l in test_list:
		print l

	for num, alph in test_list:
		print num, alph 

def dict_fn():
	list = ['apple', 'dog', 'blue']
	dict = {}

	for index, word in enumerate(list):
		dict[word] = index

	print dict

def main():
	tuple_fn()
	list_fn()
	dict_fn()

if __name__ == '__main__':
	main()

#!/bin/python3

import csv
import json
import yaml
import argparse
from pathlib import Path
import sys

# Module "Global" Variables
KEY = 'HOSTNAME'  # Key for dictionaries generated from CSV


def make_json(csvFilePath, jsonFilePath):
	# Function to convert a CSV to JSON
	# Takes the file paths as arguments

	# create a dictionary
	data = {}

	# Open a csv reader called DictReader
	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)

		# Convert each row into a dictionary
		# and add it to data
		for rows in csvReader:

			# Assuming a column named 'No' to
			# be the primary key
			key = rows[KEY]
			data[key] = rows

	# Open a json writer, and use the json.dumps()
	# function to dump data
	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
		jsonf.write(json.dumps(data, indent=4))


def make_yaml(csvFilePath, yamlFilePath):
	# Function to convert a CSV to JSON
	# Takes the file paths as arguments
 
	# create a dictionary
	data = {}

	# Open a csv reader called DictReader
	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)

		# Convert each row into a dictionary
		# and add it to data
		for rows in csvReader:
			# Assuming a column named 'No' to
			# be the primary key
			key = rows[KEY]
			data[key] = rows
 
	# Use the yaml.dump() function to write "data" to file
	with open(yamlFilePath, 'w', encoding='utf-8') as yamlf:
		yaml.dump(
			data,
			yamlf,
			sort_keys=False,
			width=72,
			indent=4
		)


def main():
	my_parser = argparse.ArgumentParser(prog="csv_convertor.py",
										 usage="%(prog)s <input CSV file> [options]",
										 description="Covert a CSV file to JSON and/or YAML",
										 add_help=True
										 )
	my_parser.add_argument('--file',
                        dest='filename',
                        action='store',
                        required=True,
                        help='CSV file to be converted')
	group_1 = my_parser.add_mutually_exclusive_group(required=True)
	group_1.add_argument('--json',
						 dest='toJSON',
						 required=False,
						 action='store_true'
						 )
	group_1.add_argument('--yaml',
						 dest='toYAML',
						 required=False,
						 action='store_true'
						 )
	group_1.add_argument('--both',
						 dest='both',
						 required=False,
						 action='store_true'
						 )
	my_parser.add_argument('--v', action='version')

	args = my_parser.parse_args()

	if args.filename:
		# Verify CSV file exists and generate output filenames
		if Path(args.filename).is_file():
			csvFilePath = args.filename
			print("Input file:\t" + csvFilePath)
			basename = Path(args.filename).stem
			jsonFilePath = basename + ".json"
			yamlFilePath = basename + ".yaml"
		else:
			print(args.filename + "not found!")
			sys.exit()
	if args.toJSON:
		make_json(csvFilePath, jsonFilePath)
		print("Output file:\t" + jsonFilePath)
	elif args.toYAML:
		make_yaml(csvFilePath, yamlFilePath)
		print("Output file:\t" + yamlFilePath)
	elif args.both:
		make_json(csvFilePath, jsonFilePath)
		print("Output file:\t" + jsonFilePath)
		make_yaml(csvFilePath, yamlFilePath)
		print("Output file:\t" + yamlFilePath)


if __name__ == '__main__':
	main()

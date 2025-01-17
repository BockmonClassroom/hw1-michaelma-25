# read_iris_MA.py
# Author: Michael Ma
# Date: 01/17/2025
# This script reads the Iris.csv dataset and prints each line.

import csv

# File path to the Iris dataset
file_path = "data/Iris.csv"

# Read and print each line of the dataset
try:
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for line in reader:
            print(line)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")

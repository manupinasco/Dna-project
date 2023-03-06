import csv
import sys
import random
import collections
import re


def main():

    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    people = []
    # Read the names and the numbers of STR into memory from file
    with open(sys.argv[1], 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            people.append(row)

    # Read the sequence of dna into memory from file
    filename = sys.argv[2]
    f = open(filename)
    dna = f.read()

    numbers = count_STR(people, dna)
        
    found = False
    found1 = False
    u = 1
    d = 1
    
    # Iterate over the different persons to see if their amounts of STR match with the amounts of this dna sequence.
    for i in range(len(people) - 1):
        for j in range(len(people[u]) - 1):
            if int(people[u][d]) == int(numbers[j]):
                found = True
            else:
                found = False
                break
            d += 1
        if found == True:
            print(people[u][0])
            found1 = True
        d = 1
        u += 1
    if found1 == False:
        print("No match")


def count_STR(people, dna):
    # Numbers will be a list with the amounts of each STR inside the dna sequence.
    numbers = []
    bigger_number = 0
    u = 1
    # Iterate over the STR given.
    for i in range(len(people[0]) - 1):
        # Count the higher number of times that the STR appears repeated consecutively.
        count = 0
        pattern = people[0][u]
        while pattern in dna:
            count += 1
            pattern += people[0][u]
        numbers.append(count)
        u += 1
    return numbers


main()
""" This file is part of the File I/O exercise.

It should be used with the two input files, fruits_1.txt and fruits_2.txt."""

def open_and_read_file(filename):
    """Opens file as a file object and returns list of contents."""

    # Write your code below.
    fruit_file = open(filename)
    fruit_data = fruit_file.read()
    fruit_data = fruit_data.split('\n')
    fruit_file.close()
    return fruit_data


def compare(lst1, lst2):
    """Takes in two lists and returns a list of items in common. """
    fruit_3 = []
    for fruit in fruit_1:
        if fruit in fruit_2:
            fruit_3.append(fruit)
    return fruit_3

#if fruit_1[fruit] == fruit_2[fruit]
#fruit_3.append(fruit)
    


# Call your functions all the way at the bottom, after they've been defined.


fruit_1 = open_and_read_file("fruits_1.txt")
fruit_2 = open_and_read_file("fruits_2.txt")

fruit_3 = compare(fruit_1, fruit_2)

print fruit_3
    


def add_nums_list(num_list):
    """Loops through a list of numbers and sums them."""

    total = 0

    for num in num_list:
        total += num

    return total


# print add_nums_list([1, 2, 3, 4, 5])


def subtract(num_list):
    """Loops through a list of numbers and takes the difference."""
    
    total = num_list[0]

    for num in range(1, len(num_list)):
        total -= num_list[num]

    return total

# print subtract([-9, 2, 3, 4, 5])


def multiply(num_list):
    """Loops through a list of numbers and returns the product of all numbers."""

    total = num_list[0]

    for num in num_list[1:]:
        total *= num

    return total

# print multiply([-1.0, 2, 3])

def divide(num_list):
    """Loops through a list of numbers and returns the quotient."""

    total = num_list[0]

    for num in num_list[1:]:
        total /= num

    return total

# print divide([10, 6.0, 1])


def square(num_list):
    """Loops through a list of numbers and returns a new list with the squares."""

    square_list = []

    for num in num_list:
        square_list.append(num ** 2)

    return square_list

# print square([10, 9, 8])


def cube(num_list):
    """Loops through a list of numbers and returns a new list with the cubes."""

    cube_list = []

    for num in num_list:
        cube_list.append(num ** 3)

    return cube_list

# print cube([2, 3, 4])
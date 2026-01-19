def square(number):
    """Calculate how many grains are on a specific square."""
    
    # Check if the square number is valid (1-64)
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")

    # The first square is 2^0, second is 2^1, etc.
    return 2 ** (number - 1)


def total():
    """Calculate the total number of grains on the whole board."""
    
    # The sum of a geometric series 2^0 + 2^1 + ... + 2^63
    # is equal to (2^64) - 1
    return (2 ** 64) - 1
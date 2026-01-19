"""Functions for calculating steps in exchanging currency."""

def exchange_money(budget, exchange_rate):
    """Calculate the value of foreign currency received."""
    # Use standard division / here to get the full float value
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """Calculate the remaining amount of the original currency."""
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """Calculate the total value of a specific denomination."""
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """Calculate the number of whole bills that can be obtained."""
    # Using floor division // ensures we get a whole number (integer)
    return int(amount // denomination)


def get_leftover_of_bills(amount, denomination):
    """Calculate the leftover amount after bills are distributed."""
    # The modulo operator % gives us the remainder
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calculate the maximum exchangeable value after fees."""
    
    # 1. Calculate the actual exchange rate including the fee (spread)
    # The spread is a percentage, so we convert it: exchange_rate * (1 + spread/100)
    actual_rate = exchange_rate * (1 + (spread / 100))
    
    # 2. Calculate the total foreign currency possible
    total_currency = budget / actual_rate
    
    # 3. Calculate how many whole bills you can get
    num_bills = total_currency // denomination
    
    # 4. Return the total value of those bills
    return int(num_bills * denomination)
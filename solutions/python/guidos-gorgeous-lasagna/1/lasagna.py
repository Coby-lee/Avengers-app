"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
"""Functions used in preparing Guido's gorgeous lasagna."""

# 1. Define your constants
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2  # Minutes per layer

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time based on the number of layers.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total preparation time in minutes.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total time elapsed (prep + baking).

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - the number of minutes the lasagna has been in the oven.
    :return: int - total elapsed time.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
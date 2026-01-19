"""Functions for implementing the rules of the classic arcade game Pac-Man."""

def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can eat a ghost.
    
    Both conditions must be True: he needs the pellet AND he must be touching the ghost.
    """
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """Verify that Pac-Man has scored.
    
    He scores if he touches a pellet OR a dot.
    """
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    """Trigger GAME OVER.
    
    He loses if he is touching a ghost AND does NOT have a power pellet.
    """
    return touching_ghost and not power_pellet_active


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger victory.
    
    He wins if he has eaten all dots AND has not lost (based on lose function logic).
    """
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)
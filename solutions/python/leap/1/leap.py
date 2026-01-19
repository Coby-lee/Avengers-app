def leap_year(year):
    # Rule 1: Must be divisible by 4
    if year % 4 == 0:
        
        # Rule 2: If it's a century (divisible by 100)...
        if year % 100 == 0:
            
            # Rule 3: ...it must also be divisible by 400
            return year % 400 == 0
            
        return True
        
    return False
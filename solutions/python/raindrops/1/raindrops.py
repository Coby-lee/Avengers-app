def convert(number):
    result = ""
    
    # Check each condition independently
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
        
    # If result is still empty, none of the conditions were met
    # We use the 'or' operator or a simple 'if' check to return the number
    return result or str(number)
def response(hey_reply):
    # Clean up whitespace from the start and end
    phrase = hey_reply.strip()
    
    # 1. Check for silence
    if not phrase:
        return "Fine. Be that way!"
    
    # 2. Determine "yelling" and "questioning" states
    # .isupper() returns True if there are letters and they are all caps
    is_yelling = phrase.isupper()
    is_question = phrase.endswith("?")
    
    # 3. Apply Bob's logic rules
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    
    if is_yelling:
        return "Whoa, chill out!"
    
    if is_question:
        return "Sure."
    
    # 4. Default response
    return "Whatever."
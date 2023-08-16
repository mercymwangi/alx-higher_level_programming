def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    outcome = 0
    initial_value = 0
    
    for char in roman_string[::-1]:
        value = roman_numerals[char]
        
        if value < initial_value:
            outcome -= value
        else:
            outcome += value
        
        initial_value = value
    
    return (outcome)

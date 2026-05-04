def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    

    # For this problem we need to first create a hashmap/dictionary
    # to link a roman signal to a value

    roman_int = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}

    # we need to have a sum value originally set at 0 to store calculated value
    sum = 0
    # We iterate through the roman string

    s = list(s) # convert to list

    # for roman_char in s:

    i = 0 

    while i <= len(s) - 1:

        current_val = roman_int[s[i]]

        # check if char is in hashmap
        if s[i] in roman_int:

            # Look ahead and check if element ahead exists and is larger
            if i + 1 < len(s) and current_val < roman_int[s[i + 1]]:
                
                # Subtraction case: subtract current value
                sum += roman_int[s[i + 1]] - current_val
                i += 2

            else:

                # Norma case
                sum += current_val
                i += 1

    return sum

# Test cases
print(romanToInt("III"))     # 3
print(romanToInt("LVIII"))   # 58
print(romanToInt("MCMXCIV")) # 1994 
print(romanToInt("IV"))      # 4
print(romanToInt("IX"))      # 9
print(romanToInt("XL"))      # 40
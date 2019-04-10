def alphabet_position(letter):
    
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"                               
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"                               
    position = 0
    found = False
    if letter in alphabet_lower:                                                
        while position < len(alphabet_lower) and not found:
            if alphabet_lower[position] == letter:
                found = True                                                    
            else:
                position = position + 1
        if found:
            return position                                                     
    if letter in alphabet_upper:                                                
        while position < len(alphabet_upper) and not found:
            if alphabet_upper[position] == letter:
                found = True                                                    
            else:
                position = position + 1
        if found:
            return position                                                    

def rotate_character(char, rot):

    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"                              
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"                              
    char_pos = alphabet_position(char)
    if char in alphabet_lower:                                                  
        rotated = char_pos + rot
        if rotated >= 26:
            rotated = (char_pos + rot) % 26                                    
            return alphabet_lower[rotated]                                      
        else:
            return alphabet_lower[rotated]                                      

    elif char in alphabet_upper:                                                
        rotated = char_pos + rot
        if rotated >= 26:
            rotated = (char_pos + rot) % 26                                     
            return alphabet_upper[rotated]                                      
        else:
            return alphabet_upper[rotated]                                      

    else:
        rotated = char
        return char                                                             
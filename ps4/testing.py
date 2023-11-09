import string

def build_shift_dict(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.        
    
    shift (integer): the amount by which to shift every letter of the 
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to 
                another letter (string). 
    '''
    assert shift >= 0 and shift < 26, "Invalid shift input, please enter between 0 and 26" 

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase

    shifted_dictionary = {}


    #Map the dictionary
    #When shift is 0 the letter will be mapped to itself (a -->a)
    #When shift is 1 the letter will be mapped to lowercase[(0 + 1) % 26] = lowercase[1] = b  
    for i in range(len(lowercase)):
        shifted_dictionary[lowercase[i]] = lowercase[(i + shift) % 26]
        shifted_dictionary[uppercase[i]] = uppercase[(i + shift) % 26]
    
    return print(shifted_dictionary)

build_shift_dict(2)
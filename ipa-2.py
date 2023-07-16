#!/usr/bin/env python
# coding: utf-8

# In[123]:


def shift_letter(letter, shift):
    '''Shift Letter.
    5 points.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if letter == " ":
        return (" ")
    elif letter == letter.upper():
        letter = str(letter)
        letter = ord(letter) - ord("A")
        letter = (letter + shift) % 26
        shift_letter = chr(letter + ord("A"))
        return (shift_letter)
    else:
        letter = letter.upper()
        letter = str(letter)
        letter = ord(letter) - ord("A")
        letter = (letter + shift) % 26
        shift_letter = chr(letter + ord("A"))
        return (shift_letter)


# In[128]:


print (shift_letter("A",1),
shift_letter("Z",28),
shift_letter("b",1),
shift_letter("w",28))


# In[59]:


def caesar_cipher(message, shift):
    '''Caesar Cipher.
    10 points.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    shifted_mess = ""
    
    for char in message:
            if char == " ":
                shifted_mess += " "
            elif char == char.upper():
                char = ((ord(char) - ord("A") + shift)) % 26
                shifted_char = chr(char + ord("A"))
                shifted_mess += shifted_char
            elif char == char.lower():
                char == char.upper()
                char = ((ord(char) - ord("A")) + shift) % 26
                shifted_char = chr(char + ord("A"))
                shifted_mess += shifted_char
            else:
                shifted_mess = "Please check your input."
                break
    return (shifted_mess)


# In[62]:


caesar_cipher("ABS ABS ABS   HI", 26)


# In[40]:


ord("A")


# In[1]:


def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.
    10 points.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    letter_shift = ord(letter_shift) - ord("A")
    if letter.isupper():
        letter = ((ord(letter) - ord("A")) + letter_shift) % 26
        letter = chr(letter + ord("A"))
    elif letter.islower():
        letter = letter.isupper
        letter = ((ord(letter) - ord("A")) + letter_shift) % 26
        letter = chr(letter + ord("A"))
    else:
        letter = ""
        
    return(letter)


# In[4]:


shift_by_letter("B","K")


# In[283]:


def vigenere_cipher(message, key):
    '''Vigenere Cipher.
    15 points.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

   Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if len(key) < len(message) and (len(message) % len(key)) == 0: 
        key = key * int(len(message) / len(key))
        key = key.upper()
        shifted_mess = ""
    
        for char, let in zip(message, key):
            if char == " ":
                shifted_mess += " "
            elif char.isupper() and let.isupper():
                start = ord(let)-(ord(let)-ord(char))
                numshift = ((ord(let)) - ord("A")) % 26
                shifted_char = chr(start + numshift)
                shifted_mess += shifted_char
            elif char.isupper() and let.islower():
                let = let.upper()
                start = ord(let)-(ord(let)-ord(char))
                numshift = ((ord(let)) - ord("A")) % 26
                shifted_char = chr(start + numshift)
                shifted_mess += shifted_char
            elif char.islower() and let.islower():
                char = char.upper()
                let = let.upper()
                start = ord(let)-(ord(let)-ord(char))
                numshift = ((ord(let)) - ord("A")) % 26
                shifted_char = chr(start + numshift)
                shifted_mess += shifted_char
            elif char.islower() and let.isupper():
                char = char.upper()
                start = ord(let)-(ord(let)-ord(char))
                numshift = ((ord(let)) - ord("A")) % 26
                shifted_char = chr(start + numshift)
                shifted_mess += shifted_char
            else:
                start = ord(let)-(ord(let)-ord(char))
                numshift = ((ord(let)) - ord("A")) % 26
                shifted_char = chr(start + numshift)
                shifted_mess += shifted_char
                break 

    elif (len(key) < len(message)) and (len(message) % len(key)) != 0:
        def the_gcf(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        mess_length = len(message)
        key_length = len(key)

        gcf = the_gcf(mess_length, key_length)

        if gcf != 1:
            remainder = key[:gcf]
        else:
            remainder = mess_length % key_length
            remainder = key[:remainder]

        key = (key * int(mess_length / key_length)) + remainder
        key = key.upper()
        
        shifted_mess = ""
    
        for char, let in zip(message, key):
            if char == " ":
                shifted_mess += " "
            elif char.isupper() and let.isupper():
                start = ord(let)-(ord(let)-ord(char))
                numshift = ((ord(let)) - ord("A")) % 26
                shifted_char = chr(start + numshift)
                shifted_mess += shifted_char
            elif char.isupper() and let.islower():
                let = let.upper()
                start = ord(let)-(ord(let)-ord(char))
                numshift = ((ord(let)) - ord("A")) % 26
                shifted_char = chr(start + numshift)
                shifted_mess += shifted_char
            elif char.islower() and let.islower():
                char = char.upper()
                let = let.upper()
                start = ord(let)-(ord(let)-ord(char))
                numshift = ((ord(let)) - ord("A")) % 26
                shifted_char = chr(start + numshift)
                shifted_mess += shifted_char
            elif char.islower() and let.isupper():
                char = char.upper()
                start = ord(let)-(ord(let)-ord(char))
                numshift = ((ord(let)) - ord("A")) % 26
                shifted_char = chr(start + numshift)
                shifted_mess += shifted_char
            else:
                start = ord(let)-(ord(let)-ord(char))
                numshift = ((ord(let)) - ord("A")) % 26
                shifted_char = chr(start + numshift)
                shifted_mess += shifted_char
                break 
            
    
    elif len(key) > len(message) and (len(key) % len(message)) != 0:
        mess_length = len(message)
        key_length = len(key)
        to_cut = key_length - (key_length % mess_length)
        key = key[:to_cut]
        key = key.upper()
        
        shifted_mess = ""
    
        for char, let in zip(message, key):
            if char == " ":
                shifted_mess += " "
            elif char.isupper() and let.isupper():
                start = ord(let)-(ord(let)-ord(char))
                numshift = ((ord(let)) - ord("A")) % 26
                shifted_char = chr(start + numshift)
                shifted_mess += shifted_char
            elif char.isupper() and let.islower():
                let = let.upper()
                start = ord(let)-(ord(let)-ord(char))
                numshift = ((ord(let)) - ord("A")) % 26
                shifted_char = chr(start + numshift)
                shifted_mess += shifted_char
            elif char.islower() and let.islower():
                char = char.upper()
                let = let.upper()
                start = ord(let)-(ord(let)-ord(char))
                numshift = ((ord(let)) - ord("A")) % 26
                shifted_char = chr(start + numshift)
                shifted_mess += shifted_char
            elif char.islower() and let.isupper():
                char = char.upper()
                start = ord(let)-(ord(let)-ord(char))
                numshift = ((ord(let)) - ord("A")) % 26
                shifted_char = chr(start + numshift)
                shifted_mess += shifted_char
            else:
                start = ord(let)-(ord(let)-ord(char))
                numshift = ((ord(let)) - ord("A")) % 26
                shifted_char = chr(start + numshift) 
                shifted_mess += shifted_char
                break 
    
    else:
        key = key.upper()
        shifted_mess = ""
    
        for char, let in zip(message, key):
            if char == " ":
                shifted_mess += " "
            elif char.isupper() and let.isupper():
                start = ord(char) - ord("A")
                shift = ord(let) - ord("A")
                shifted_char = chr((start + shift) % 26 + ord("A"))
                shifted_mess += shifted_char
            elif char.isupper() and let.islower():
                let = let.upper()
                start = ord(let)-(ord(let)-ord(char))
                numshift = ((ord(let)) - ord("A"))
                shifted_char = chr((start + numshift) % 26)
                shifted_mess += shifted_char
            elif char.islower() and let.islower():
                char = char.upper()
                let = let.upper()
                start = ord(let)-(ord(let)-ord(char))
                numshift = ((ord(let)) - ord("A"))
                shifted_char = chr((start + numshift) % 26)
                shifted_mess += shifted_char
            elif char.islower() and let.isupper():
                char = char.upper()
                start = ord(let)-(ord(let)-ord(char))
                numshift = ((ord(let)) - ord("A"))
                shifted_char = chr((start + numshift) % 26)
                shifted_mess += shifted_char
            else:
                start = ord(let)-(ord(let)-ord(char))
                numshift = ((ord(let)) - ord("A"))
                shifted_char = chr((start + numshift) % 26)
                shifted_mess += shifted_char
                break 
    return (shifted_mess)


# In[285]:


vigenere_cipher("DOG","CAT")


# In[41]:


def vigenere_cipher(message, key):
    '''Vigenere Cipher.
    15 points.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

   Returns
    -------
    str
        the message, shifted appropriately.
    '''
    key = key.upper()
    
    if len(key) < len(message) and (len(message) % len(key)) == 0: 
        key = key * int(len(message) // len(key))

    elif (len(key) < len(message)) and (len(message) % len(key)) != 0:
        def the_gcf(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        mess_length = len(message)
        key_length = len(key)

        gcf = the_gcf(mess_length, key_length)

        if gcf != 1:
            remainder = key[:gcf]
        else:
            remainder = key[:mess_length % key_length]

        key = (key * int(mess_length // key_length)) + remainder
        
    elif len(key) > len(message) and (len(key) % len(message)) != 0:
        mess_length = len(message)
        key_length = len(key)
        to_cut = key_length - (key_length % mess_length)
        key = key[:to_cut]
        
    else:
        key = key
        
    
    shifted_mess = ""
    
    for char, let in zip(message, key):
        if char == " ":
            shifted_mess += " "
        else:
            char = char.upper()
            let = let.upper()
            
            char = ord(char) - ord("A")
            let = ord(let) - ord("A")
            
            shifted_char = (char + let) % 26
            shifted_char = chr(shifted_char + ord("A"))
        
            shifted_mess += shifted_char
    return shifted_mess


# In[51]:


vigenere_cipher("ZAa", "B")


# In[97]:


def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
   
    #STEP 2: message is a multiple
    if (len(message) % shift) == 0:
        message = message
    else:
        while (len(message) % shift) != 0:
            message += "_"
   
    shifted_mess = ""
    for i in range(len(message)):
        i = (i // shift) + (len(message) // shift) * (i % shift)
        shifted_mess += message[i]
    
    return shifted_mess
            


# In[104]:


scytale_cipher("ALGORITHMS_ARE_IMPORTANT",8)


# In[220]:


def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    ciphered_message = ""
    length = len(message)
    
    for i in range(shift):
        for j in range(i, length, shift):
            ciphered_letter = message[j]
            ciphered_message += ciphered_letter

    return ciphered_message


# In[225]:


scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8)


# In[ ]:





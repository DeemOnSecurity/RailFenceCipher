def create_array(key: int) -> list:
    """
    Creates an array for the use of our rail cipher.

    For example:
        Given the key 3, it creates an array like:
        [[    ],
         [    ],
         [    ]]

        We will later populate the list like so:
        [[H   O   R   ]
         [ E L   O L !]
         [  L   W   D ]]

    :param key: The cipher key, number of rows to make in our array.
    :return list: The list of lists to be used later.
    """
    array = []

    """
    range() starts from 1, then goes to the value before whatever is after the ',', 
    because of this, we have to add one to the key.
    """
    for i in range(1, key + 1):
        array.append([])

    return array


def encode(text: str, key: int):
    """
    Encodes our text(str) in a rail cipher, given there is a key(int).

    1. Turns the given text into a list so we can pop(0) it later.
    2. Creates an array, see create_array() documentation.
    3. Iterates through the array up and down, popping values from the text into the array.
    4. Joins the array.
    5. Returns the array as a string.

    :param text: Text to be encoded.
    :param key: The cipher key, number of rows to make in our array.
    :return: Rail cipher encoded text.
    """
    # 1
    text = list(text)

    # 2
    array = create_array(key)

    # 3
    try:
        while text:
            """
            Going from 0 (the start of the index) to the last row (key value),
            pops the first value present in the list into the given row in the array.
            
            Given n = 4
            Row 1 -> Row 2 -> Row 3 -> Row 4
            """
            for row in range(0, key):
                array[row].append(text.pop(0))

            """
            Tricky part, going from the bottom up. We never double up at the top or bottom
            of the cipher, so we need to skip the bottom and top rows, as we will iterate 
            through again in this while loop.
            
            Given n = 4
            Row 3 -> Row 2
            """
            for row in reversed(range(1, key - 1)):
                array[row].append(text.pop(0))

    except IndexError:
        """
        The while loop will continue until it hits an IndexError, row.e. no more values to pop()
        """
        pass

    # 4
    array = sum(array, [])

    # 5
    return ''.join(array)


def decode(text: str, key: int):
    """
    Decodes our rail cipher text(str), given there is a key(int)

    1. Determines the length of the given text
    2. Creates a list of the range(len(text)), i.e. a 5 len string would be [0,1,2,3,4]
    3. Creates an array, see create_array() documentation.
    4. Iterates through the array up and down, popping values from the range list into the array.
    5. Joins the array.
    6. Creates an empty list the length of the text to be used later.
    7. Moves characters from the text into the proper index location in our temporary list.
    8. Returns the joined list.

    :param text: Text to be decoded.
    :param key: The cipher key, number of rows to make in our array.
    :return: Decoded text.
    """

    # 1
    length = len(text)

    # 2
    """
    This is the big trick to the puzzle. To decode the rail cipher, we just
    follow the encoding steps again, but instead of doing some wizardry, we
    just use the list range, which after encoding will give us the index
    locations of the encoded text.
    """
    lst = []
    for i in range(length):
        lst.append(i)

    # 3
    array = create_array(key)

    # 4
    """
    This is the exact same code in the encode() method, just with text replaced by lst.
    """
    try:
        while lst:
            for row in range(0, key):
                array[row].append(lst.pop(0))
            for row in reversed(range(1, key - 1)):
                array[row].append(lst.pop(0))
    except IndexError:
        pass

    # 5
    array = sum(array, [])

    # 6
    lst = [''] * len(text)

    # 7
    """
    Here we send the characters in our scrambled text to the proper index position determined earlier.
    
    e.g.
    Hoell
    [0,4,1,3,2]
    
    H[0] = lst[0]
    H[1] = lst[4]
    etc.
    
    """
    for character, index in zip(text, array):
        lst[index] = character

    # 8
    return ''.join(lst)


if __name__ == '__main__':
    import datetime, shutil

    term_size = shutil.get_terminal_size(fallback=(80, 20)).columns
    start = datetime.datetime.now()
    encoded_text = encode(open('StateOfTheUnion1864.txt').read(), 200)
    print(encoded_text + '\n')
    print(''.center(term_size, '-') + '\n')
    print(decode(encoded_text, 200))
    print(f'\n\n {datetime.datetime.now() - start} seconds'.center(term_size, '-'))

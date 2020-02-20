def fence(item: str or list, key: int) -> str:
    """
    This generator function is a lot more concise than our work in tutorial(),
    however (as you can see) it is a lot more math intensive and may take more
    time to understand.

    This function takes advantage of the recognizable pattern in the fence cipher,
    it looks for the space between the values in the first row, then does math
    to get the v shape we're looking for:

    [H . . . O]
    [. E . L .]
    [. . L . .]

    As you can see, there is 3 empty spaces between the first row, 1 in the second
    and meeting in the middle. We can calculate that the index position of the
    character in each row will be x + 1 and x - 1 where x is the position of the
    character in the row above it.

    This is literally a text parabola.

    :param item: ITEM to encode, this can be the text or the length range.
    :param key: The cipher key, number of rows to make in our array.
    :return: Yields the encoded text.
    """

    """
    Takes over the function of create_array() in our tutorial example, each iteration is the next row.
    """
    for row in range(key):

        """
        The key - 1 * 2 in step is accounting for python indices, which start at 0 always then multiplying itself
        to account for the next position used in the array.
        """
        step = (key - 1) * 2

        """
        A truthy statement testing if it is in the first row or the last, remember, we have to subtract 1 to account
        for the python indices.
        """
        border = row in (0, key - 1)

        """
        The python range() statement takes 3 arguments, the starting point, stopping point, and the step, in this
        case we are going from 0 to the end of the string or list, stepping our predetermined amount.
        """
        for i in range(0, len(item), step):

            """
            This is our parabolic method right here.
            """
            for index in (i + row,) if border else (i + row, i + step - row):

                """
                Ensure there is going to be text at the index position (not over, or we will get an IndexError)
                """
                if index < len(item):
                    """
                    This is a generator function, which returns similar to if we were returning a list, this function
                    is returning the value at the index position.
                    """
                    yield item[index]


def encode(string: str, key: int) -> str:
    """
    Our encode function is a lot simpler, given all of the hard work is done in fence(),
    we are just joining the list, i.e. turning the list into a string.

    :param string: Text to encode.
    :param key: The cipher key, number of rows to make in our array.
    :return: The encoded string.
    """
    return ''.join(fence(string, key))


def decode(string: str, key: int) -> str:
    """
    This is similar to our tutorial decode() function, but is a lot shorter thanks to the
    fence() function.

    :param string: Text to decode.
    :param key: The cipher key, number of rows to make in our array.
    :return: The decoded string.
    """
    lst = [''] * len(string)
    for character, index in zip(string, fence(range(len(string)), key)):
        lst[index] = character
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

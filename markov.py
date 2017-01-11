from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file_path).read()
    return contents
    # your code goes here

    # return "This should be a variable that contains your file text as one long string"


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (index1, index2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    #Split our list into a list of words
    word_list = text_string.split()

    #Loop through our word_list

    for index1 in range(len(word_list) - 2):
        index2 = index1 + 1
        index3 = index2 + 1

        current_tuple = (word_list[index1], word_list[index2])
        next_word = word_list[index3]

        #inserting our tuple and values into dict
        if current_tuple in chains:
            current_values = chains[current_tuple]
            #if the current pair exists as a key, append the value list
            current_values.append(next_word)
        else:
            chains[current_tuple] = [next_word]
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text_list = []
    original_key = choice(chains.keys())
    original_value = choice(chains[original_key])
    text_list.append(original_key[0])
    text_list.append(original_key[1])
    text_list.append(original_value)

    while (text_list[-2], text_list[-1]) in chains:
        new_key = (text_list[-2], text_list[-1])
        new_value = choice(chains[new_key])
        text_list.append(new_value)


    return " ".join(text_list)

input_path = "gettysburg.txt"

# # Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

chains = make_chains(input_text)

print make_text(chains)


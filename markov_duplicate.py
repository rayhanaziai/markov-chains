from random import choice
import sys
import string 



def open_and_read_file():
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = sys.argv[1]
    open_contents = open(contents).read()
    return open_contents
    # your code goes here

    # return "This should be a variable that contains your file text as one long string"


def make_chains(text_string, n):
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


    for index1 in range(len(word_list) - n):

        current_lst = []
        for i in range(index1, index1+n):
            word = word_list[i]
            current_lst.append(word)

        current_tuple = tuple(current_lst)

        next_word = word_list[index1+n]

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
    text_list.append(original_key[0].title())
    text_list.append(original_key[1])
    text_list.append(original_value)

    while (text_list[-2], text_list[-1]) in chains:
        new_key = (text_list[-2], text_list[-1])
        new_value = choice(chains[new_key])
        text_list.append(new_value)


    return " ".join(text_list)

# input_path = "gettysburg.txt"

# # Open the file and turn it into one long string
input_text = open_and_read_file()

chains = make_chains(input_text, 3)

print make_text(chains)


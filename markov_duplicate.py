from random import choice
import sys
import string 
import send_tweet

n = int(raw_input("What value of n would you like to use for your n-gram?"))


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

    #Loop through our word_list until "n" items remain
    for index in range(len(word_list) - n):

        keys_list = []
        # loop through n items of word_list, and insert it into keys_list
        for word_index in range(index, index+n):
            keys_list.append(word_list[word_index])

        #turn keys_list into a tuple
        keys_tuple = tuple(keys_list)

        current_value = word_list[index+n]

        #inserting our tuple and values into dict
        #if the current pair exists as a key, append the value list
        if keys_tuple in chains:
            chains[keys_tuple].append(current_value)
        # otherwise if key doesn't exist, add key and add value to dictionary
        else:
            chains[keys_tuple] = [current_value]
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text_list = []
    original_key = choice(chains.keys())
    original_value = choice(chains[original_key])

    for item in original_key:
        text_list.append(item)

    text_list.append(original_value)

    while tuple(text_list[-n:]) in chains:
        new_key = tuple(text_list[-n:])
        new_value = choice(chains[new_key])
        text_list.append(new_value)

    text_list[0] = text_list[0].title()

    final_tweet = ""
    long_tweet = " ".join(text_list)
    for i in range(118):
        final_tweet = final_tweet + long_tweet[i]
    final_tweet = final_tweet + " #hackbrightgracejan17"

    return final_tweet

# input_path = "gettysburg.txt"

# # Open the file and turn it into one long string
input_text = open_and_read_file()

chains = make_chains(input_text)

final_tweet = make_text(chains)
# print make_text(chains)

send_tweet.post_tweet(final_tweet)

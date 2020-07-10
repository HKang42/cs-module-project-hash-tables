import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

words = words.replace('\n', ' ').split()

dict = {}

for i in range(0, len(words)):

    dict[words[i]] = list( set( words[i+1:] ) )


# TODO: construct 5 random sentences
# Your code here

def start_chooser(dict):
    """
    Given a markov generator dictionary, choose a random start word.
    Returns None if a start word could not be found
    """
    break_count = len(dict) * 1000
    count = 0

    while count < break_count:
        word = random.choice(list(dict.keys()))
        
        if word[0].isupper():
            return word
        
        elif word[0] == '"' and word[1].isupper():
            return word
        
        count += 1

    return None

def is_stop(word):
    """ 
    Given a word, return True if it is a stop word or False otherwise. 
    """
    end_chars = ['.', '?', '!']

    if word[-1] in end_chars:
        return True
    
    elif len(word) < 2:
        return False

    elif word[-2] in end_chars and word[-1] == '"':
        return True
    
    else:
        return False


stop = 5
count = 0

word = start_chooser(dict)

string = ''

while count <= 5:

    string += word + ' '

    if is_stop(word) == True:
        print(string, '\n')

        string = ''

        word = start_chooser(dict)

        count += 1
        
    else:
        word = random.choice( dict[word] )

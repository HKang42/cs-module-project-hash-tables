# Your code here

# We can either:
# Use words as the keys and print by descending value then descending key
# Or
# Use counts as the keys and print by descending key then descending value


# Let's try option 2

# Grab text and format
with open("robin.txt") as f:
    text = f.read()

text = text.lower().replace('\n', ' ')

# Remove punctuation
punct = set(['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&'])
text = "".join(char for char in text if char not in punct)

# Convert to a list of words
text = text.split()

# Create a set of our words so we don't loop through redundant entries
word_set = set(text)

# Create our dictionary where each key is the number of times a word appears
# and each value is the number of words with that count
# We also track the length of the longest word to format our print statements later
count_dict = {}
longest = 0

for word in word_set:
    count = text.count(word)

    longest = max(longest, len(word))

    if count in count_dict:
        count_dict[count].append(word)

    else:
        count_dict[count] = [word]


# Choose how many entries we want to display
num_entries = 10
entry_counter = 1

# Loop through sorted versions of our dictionary and word lists
for count in sorted(count_dict, reverse=True):
    
    for word in sorted(count_dict[count]):

        # The hash marks should be left justified two spaces after the longest possible word.
        print_str = str(word).ljust(longest + 2, " ").ljust(longest + count + 2, "#")
        print(print_str)
        
        if entry_counter >= num_entries:
            break
        entry_counter += 1
    
    # need this to break the nested loop -> https://stackoverflow.com/a/654002/13486401
    else:
        continue
    break
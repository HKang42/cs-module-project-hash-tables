punct = set(['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&'])

def word_count(s):
    # Your code here
    dict = {}

    s_list = s.split()

    for word in s_list:
        
        # remove punctuation characters and make string lower case
        word = "".join(char for char in word if char not in punct).lower()

        # if word was composed entirely of punct characters, then we skip the word
        if word == '':
            continue

        if word in dict:
            dict[word] += 1

        else:
            dict[word] = 1

    return dict

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
# I'm pretty sure using a set is better than a dictionary here.
# Can adapt the solution to just using dictionary.keys if a hash table is required

def no_dups(s):
    # Your code here
    word_set = set()
    
    s_list = s.split()

    output = ''

    for word in s_list:
        if word in word_set:
            continue
        
        else:
            word_set.add(word)
            output += word + ' '

    return output[0:-1]

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    i = word.find('th') # Look for the first occurence of `th`
    if i == -1: # if no occurrence return 0 (recursive base case)
        return 0
    return 1 + count_th(word[i+2:])

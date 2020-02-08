'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # base case is
    # we need to check first two letters, then next two and so on because order matters
    # list comprehensions will help here
    # letters_list = [letter for letter in word]
    th_occurences = 0
    index = 0
    # base case below
    if len(word) < 2:
        return 0
    elif word[0] == "t" and word[1] == "h" and index < len(word) - 1:
        th_occurences += 1
        index += 1
        return count_th(word[1:]) + 1
    else:
        index += 1
        return count_th(word[1:])


count_th("THtHThth")

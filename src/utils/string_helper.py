def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    count = 0
    for c in s.lower():
        if c in "aeiou":
            count+=1
    return count

def count_letter_in_list(data):
    count = {}
    
    for i in data:
        if i in count:
            count[i] +=1
        else:
            count[i] = 1
    return count

def count_more_letter_in_list(data):
    count = {}
    more_letter = {}
    arr =set()
    for i in data:
        if i in count and count[i] >= 1:
            more_letter[i] += 1
            arr.add(i)
        else:
            count[i] = 1
            more_letter[i] = 1
    return more_letter,list(arr)

from collections import Counter

def count_lettes(li):
    return Counter(li)


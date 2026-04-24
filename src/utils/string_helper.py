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
    duplicates = []
    for i in data:
        if i in count:
            count[i] += 1
            if count[i] == 2:
                duplicates.append(i)
        else:
            count[i] = 1
    return count, duplicates

from collections import Counter

def count_lettes(li):
    return Counter(li)


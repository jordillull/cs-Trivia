#!/usr/bin/env python3

def groupAnagrams(arr):
    d = {}
    for word in arr:
        # The key is composed by the sorted non blank characteres of the word
        # in lower case
        key = ''.join(sorted(word.lower().replace(' ', '')))
        if key not in d:
            d[key] = [word]
        else:
            d[key] += [word]

    return list(d.values())



if __name__ == "__main__":
    authors = ["Arrigo Boito", "Edward Gorey", 
            "Tobia Gorrio", "Ogdred Weary", 
            "Regera Dowdy", "Vivian Darkbloom", 
            "Damon Albarn", "Dan Abnormal", 
            "Vladimir Nabokov", "Vivian Bloodmark", 
            "Blavdak Vinomori", "Dave Barry", 
            "Ray Adverb"]

    print(authors)
    print(groupAnagrams(authors))

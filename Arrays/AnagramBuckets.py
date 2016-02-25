'''
Input - List<String> ["star", "rats", "ice", "cie", "arts"] 
print all anagrams in buckets: 
["star", "rats", "arts"] 
["ice", "cie"] 

The signature of unimplemented method is given:

public void anagramBuckets(List<String> input);
'''

from collections import defaultdict

buckets = defaultdict(list)
words = ["star", "rats", "ice", "cie", "arts"]

for i in xrange(len(words)):
    sort = ''.join(sorted(words[i]))
    buckets[sort].append(words[i])

print(words)
print(list(buckets.values()))
    

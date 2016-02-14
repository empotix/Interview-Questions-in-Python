'''
Code a function that receives an array with duplicates and returns a new array keeping the original order of the elements but with the duplicates removed. 

For example, if the input were

@[ @"dog", @"cat", @"dog", @"fish" ]
the output would be


@[ @"dog", @"cat", @"fish" ]
Tell the complexity of the solution.
'''

from collections import OrderedDict

array = ["dog", "cat", "dog", "fish" ]
hash_table = OrderedDict()

for word in array:
    if not hash_table.get(word,None):
        hash_table[word] = 1

print(hash_table.keys())
        
'''
You're given a dictionary of strings, and a key. Check if the key is composed of an arbitrary number of concatenations of strings from the dictionary. For example: 

dictionary: "world", "hello", "super", "hell" 
key: "helloworld" --> return true 
key: "superman" --> return false 
key: "hellohello" --> return true
'''
from Trie import Trie

words = ["world", "hello", "super", "hell" ]
trie = Trie()

for word in words:
    trie.insert(word, 1)

def search(root, key, new_start = False):
    
    if root == None:
        return False
    
    if new_start:
        if not root.children.get(key[0], None):
            return False
    
    if(len(key) == 0):
        if root.data == 1:
            return True
        return False
        
    #Since we still have characters left, we search for the child node using the next
    #character in line
    child = root.children.get(key[0], None)
    
    if child:
        return search(child, key[1:])
    else:
        return search(trie.root, key[1:], True)

print(search(trie.root, "helloworld"))

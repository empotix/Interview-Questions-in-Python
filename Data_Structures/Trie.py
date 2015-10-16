'''
Created on Oct 15, 2015

@author: gaurav
'''
#Aympotitic complexity for a trie search of insert depends on the length of the
#string you are working with. That means that this means it is LINEAR IN THE LENGTH
#OF THE KEY.

#Compared to hash tables whose looks up becomes slower after we add a lot of keys
#that cause collisions, tries will always remain linear wrt to their own length.
#That being said, tries may need n nodes to store a n length word while a hash
#table only needs one node per word

#MAJOR APPLICATION: Auto complete in the Google Search engine

class Trie(object):
    '''
    classdocs
    '''
    def __init__(self, root = None):
        '''
        Constructor
        '''
        self.root = root
        
    def search(self, root, key): 
        
        if not root:
            return
        
        #If we run out of characters in our key, there should be data present at the current node
        #If there is, return the value associated with the current node
        if len(key) == 0:
            if root.data:
                print("Associated value with key is {0}".format(root.data))
                return root.data
        
        #Since we still have characters left, we search for the child node using the next
        #character in line
        child = root.children.get(key[0], None)
        
        #If no child is present, it means no such key is present in the trie
        if not child:
            print("No such key is present in the trie")
            return 
        
        #Recursively call search on the child node with the modified key value
        return self.search(child, key[1:])
        
    def insert(self, key, value):
        self._insertIntoTrie(self.root, key, value)
        
        
    def _insertIntoTrie(self, root, key, value):
        
        #If the key is on its last character, create a new child node BUT with data this time
        #The data is the value
        if len(key) == 1:
            root.children[key[0]] = self.TrieNode(value)
            return
        
        #If this is the first ever insert statement, create a root node with no data and no children
        #And then call insert on the root node
        if not self.root: 
            self.root = self.TrieNode(None)
            self._insertIntoTrie(self.root, key, value)
        
        else:
            #Get the child node depending on the current character. If it is not there, create one 
            #with no data and make it the child node.
            child = root.children.get(key[0], None)
            if not child:
                root.children[key[0]] = self.TrieNode(None)
                child = root.children.get(key[0])
            
            #Calling insert on the child with the remaining key
            self._insertIntoTrie(child, key[1:], value)
            
         
    class TrieNode(object):
        
        def __init__(self, data):
            #Data is null unless we are storing a character in the node
            self.data = data
            
            #Number of children should be 26 at max (26 alphabets of english). These children
            #should be TrieNodes themselves. The keys are the alphabets and the values are the 
            #pointers to the TrieNodes
            self.children = {}
    
def main():
    t = Trie()
    t.insert("abc", 1)
    t.insert("abd", 2)
    t.insert("abcd", 3)
    print(t.search(t.root, "abc"))
    print(t.search(t.root, "abd"))
    print(t.search(t.root, "abcd"))
    print(t.search(t.root, "abcde"))
    
if __name__ == "__main__":
    main()
        
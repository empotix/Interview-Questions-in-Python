
def findLongestChainForWord(word, w, count):
    new_count = count;
    current_max_count = count;
    
    for i in xrange(0, len(word)):
        new_word = word[:i] + word[i+1:]
        if new_word and new_word in w:
            new_count = findLongestChainForWord(new_word, w, count + 1)
            if new_count > current_max_count:
                current_max_count = new_count
                
    return current_max_count;



def longest_chain(w):
    max_count = 0
    max_word = ""
    for word in w[::-1]:
        if len(word) < max_count:
            break
        count = findLongestChainForWord(word,w,1)
        if count > max_count:
            max_count = count
            max_word = word
        
    print(max_count)
    print(max_word)

w = ['a','b','bc','bca','bda','bdca']
longest_chain(w)
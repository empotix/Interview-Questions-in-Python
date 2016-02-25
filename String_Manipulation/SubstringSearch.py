'''
"Given a string Sting="ABCSC" Check whether it contains a Substring="ABC"? 
1)If no , return "-1". 
2)If yes , remove the substring from string and return "SC"."
'''

def findSubstring(word, sub):
    hash_word = 0
    hash_substring = hash_value(sub, 0, len(sub), 0)
    
    for i in range(0, len(word)-len(sub)+1):
        hash_word = hash_value(word, i, len(sub), hash_word)
        if(hash_word == hash_substring):
            return i
    return -1
        

def hash_value(string, start_index, length, previous_value):
    
    value  = 0
    base = 101
    
    #If this is the first time the hash value is being computed
    if(previous_value == 0):
        for i, char in enumerate(string[0:length]):
            value += ord(char) * pow(base,length-i-1)  
     
    #Removing the hash contribution of the last character and adding that of the new character       
    else:   
        old_char = string[start_index-1]
        old_char_hash_value = (ord(old_char) * pow(base,length-1))
        new_char = string[start_index+length-1]
        new_char_hash_value = ord(new_char)
        
        value = (base * (previous_value - old_char_hash_value)) + new_char_hash_value * pow(base,0)
                 
    return value
    

def main():
    word = "CBABCSC"
    sub = "SC"
    index = findSubstring(word, sub)
    
    if index != -1:
        print(word[0:index]+word[index+len(sub):])
    
    
if __name__ == '__main__':
    main()
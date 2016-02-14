'''
Implement a method called printNonComments() which prints out a extract of text with comments removed. 

For example, the input: 

hello /* this is a 
multi line comment */ all 

Should produce: 

hello 
all 

You have access to a method called getNextLine() which returns the next line in the input string.'''



def printWithoutComments(string):
    
    #Bit that keeps track of whether we are looking for start or end of comment
    #Currently set to look for start
    start_end = 0
    lines = string.split('\n')
    for line in lines:
        if start_end:
            comment = '*/' 
            if comment in line:
                print(line.split(comment)[1])
                start_end = 0
            else: 
                print(line)
        else:
            comment = '/*'
            if comment in line:
                print(line.split(comment)[0])  
                start_end = 1          
            else:
                print(line)


string = '''hello /* this is a 
multi line comment */ all '''
printWithoutComments(string)

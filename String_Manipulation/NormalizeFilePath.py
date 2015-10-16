'''
Created on Oct 15, 2015

@author: gaurav
'''

#Given a string representing relative path write a function which normalizes this path (i.e. replaces ".."). 
#Example: 
#input: /a/b/../foo.txt 
#output: /a/foo.txt

def normalizeFilePath(s):
    path_split = s.split('/')
    required = []
    required.append(path_split[1]) 
    required.append(path_split[-1]) 
    print('/' + '/'.join(required))

if __name__ == '__main__':
    normalizeFilePath("/a/b/c/d/foo.txt")
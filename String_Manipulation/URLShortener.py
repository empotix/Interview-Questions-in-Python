import math
directory = {}

def shorten_url(url):
    
    #Generating the id with which this url will be stored
    ids = directory.keys()
    current_url_id = max(ids) + 1 if len(ids) > 0 else 1
    
    #Need to convert this base 10 id to base 62 considering we have A-Z, a-z & 0-9
    base62_id = convert_base62(current_url_id)
    
    #Shortening the url by mapping the numbers to characters
    shortUrl = "https://tinyurl.com/"+findTinyUrlStringForBase62Id(base62_id)
    
    directory[current_url_id] = {"original":url, "short":shortUrl}
    return shortUrl
    
def findTinyUrlStringForBase62Id(base62_id):
    
    finalShortUrl = []
    for n in base62_id:
        if n < 26:
            finalShortUrl.append(chr(n+97))
        elif n < 52:
            finalShortUrl.append(ord(n+39))
        else:
            finalShortUrl.append(ord(n-5))
    return ''.join(finalShortUrl)
    
def convert_base62(num):
    digits = []
    while num > 0:
        remainder = num % 62
        digits.append(remainder)
        num = num / 62
    return digits[::-1]

def longen_url(url):
    chars = url.split('/')[-1]
    num = []
    
    #Converting the url short to base 62 char representation
    for ch in chars:
        if ch > 96:
            num.append(ord(ch)-97)
        elif ch > 64:
            num.append(ord(ch)-39)
        else:
            num.append(ord(ch)+4)
     
    #Converting base 62 number back to base 10 and finding the corresponding 
    #normal url
    final_value = 0;
    num = num[::-1]
    for i in xrange(len(num)-1,-1,-1):
        final_value += num[i] * math.pow(62, i)       
    
    return directory[int(final_value)]
    
print(shorten_url("https://www.google.com/gkeswani91"))
print(shorten_url("https://www.google.com/gkeswani92"))
print(shorten_url("https://www.google.com/gkeswani93"))
print(shorten_url("https://www.google.com/gkeswani94"))
print(shorten_url("https://www.google.com/gkeswani95"))
print(shorten_url("https://www.google.com/gkeswani96"))
print(shorten_url("https://www.google.com/gkeswani97"))
print(shorten_url("https://www.google.com/gkeswani98"))
print(shorten_url("https://www.google.com/gkeswani99"))
print(longen_url("https://tinyurl.com/a"))
print(longen_url("https://tinyurl.com/b"))
print(longen_url("https://tinyurl.com/c"))
print(longen_url("https://tinyurl.com/d"))
print(longen_url("https://tinyurl.com/e"))
print(longen_url("https://tinyurl.com/f"))
print(longen_url("https://tinyurl.com/g"))
print(longen_url("https://tinyurl.com/h"))
print(longen_url("https://tinyurl.com/i"))
print(longen_url("https://tinyurl.com/j"))
    

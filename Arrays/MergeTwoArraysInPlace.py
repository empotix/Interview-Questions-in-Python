'''
// merge sorted arrays 'a' and 'b', each with 'length' elements, 
// in-place into 'b' to form a sorted result. assume that 'b' 
// has 2*length allocated space. 
// e.g. a = [1, 3, 5], b = [2, 4, 6] => b = [1, 2, 3, 4, 5, 6] 

//how to do it without rearanging the b array
'''

a = [1, 3, 5]
b = [2, 4, 6]

pointerA = len(a) - 1
pointerB = len(b) - 1
mainPointer = len(a) + len(b) - 1

#Padding 0's to make B have enough space for both arrays elements
for i in range(pointerB, mainPointer):
    b.append(0)

while pointerB >= 0 and pointerA >= 0:
    if(a[pointerA] > b[pointerB]):
        b[mainPointer]=a[pointerA]
        pointerA-=1
    else:
        b[mainPointer]=b[pointerB]
        pointerB-=1
    mainPointer-=1

if (pointerB == -1 and pointerA !=-1):
    for i in range(pointerA,-1,-1):
        b[mainPointer]=a[i]
        mainPointer-=1
elif (pointerA == -1 and pointerB !=-1):
    for i in range(pointerB,-1,-1):
        b[mainPointer]=b[i]
        mainPointer-=1

print(b)
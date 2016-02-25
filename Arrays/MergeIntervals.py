'''
Given two arrays/Lists (choose whatever you want to) with sorted and non 
intersecting intervals. Merge them to get a new sorted non intersecting 
array/list. 

Eg: 
Given: 
Arr1 = [3-11, 17-25, 58-73]; 
Arr2 = [6-18, 40-47]; 

Wanted: 
Arr3 = [3-25, 40-47, 58-73];
'''

class Interval:
    lower = None
    upper = None
    
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper
    
    #Checks if the two intervals overlap with each other
    def isOverlapping(self, ob):
        if (ob.lower > self.lower and ob.lower < self.upper) \
            or (ob.upper > self.lower and ob.upper < self.upper) :
            return True
        
        return False

    #Pass in a set of interval elements to be merged
    def merge(self, interval):
        lowerBound = min(self.lower, interval.lower)
        upperBound = max(self.upper, interval.upper)
        return Interval(lowerBound, upperBound)

def findIntervalPosition(interval, arr1):
    for i in xrange(len(arr1)-1,-1,-1):
        if interval.lower > arr1[i].lower:
            return i+1;
        
def mergeNewInterval(arr1, index):
    
    lower = index - 1
    upper = index + 1
    
    while lower >= 0 or upper < len(arr1):
        if lower >= 0:
            if arr1[index].isOverlapping(arr1[lower]):
                newInterval = arr1[index].merge(arr1[lower])
                arr1.pop(index)
                arr1.pop(lower)
                arr1.insert(lower, newInterval)
                index = index - 1
                lower = lower - 1
                upper = upper - 1
            else:
                lower = -1  #As soon as one lower element does not overlap, no other element
                            #below it will overlap. So no need to check
        
        if upper < len(arr1):
            if arr1[index].isOverlapping(arr1[upper]):
                newInterval = arr1[index].merge(arr1[upper])
                arr1.pop(upper)
                arr1.pop(index)
                arr1.insert(index, newInterval)
            else:
                upper = len(arr1) + 1

def main():
    arr1 = [Interval(3,11), Interval(17,25), Interval(58,73)]
    arr2 = [Interval(6,18), Interval(40,47)]
    
    for interval in arr2:
        
        #Insert the element into the right position in arr1
        index = findIntervalPosition(interval, arr1)
        arr1.insert(index, interval)
        mergeNewInterval(arr1, index)
    
    for interval in arr1:
        print("({0}-{1})".format(interval.lower, interval.upper))               

if __name__ == "__main__":
    main()


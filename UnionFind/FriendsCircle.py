class Union:
    friends = None
    def __init__(self, i):
        if isinstance(i, list):
            self.friends = i
        else:
            self.friends = [i]
    
    def mergeFriendCircle(self, b):
        return Union(self.friends + b.friends)
        
def findFriendCircleOf(i, friend_circles):
    for circle in friend_circles:
        if i in circle.friends:
            return circle
    return None


def friendCircles( friends):
    friend_circles = []
    
    #Putting each person in their own friend circle
    for i in xrange(len(friends)):
        friend_circles.append(Union(i))
    
    for i,friendships in enumerate(friends):
        friend_circle = findFriendCircleOf(i, friend_circles)
        
        #Checking who the current person is linked to
        for j, friend in enumerate(friendships):
            if i != j:
                if friend == 'Y':
                    new_friend_circle = findFriendCircleOf(j, friend_circles)
                    
                    #If i and j are not already in the same friend circle, 
                    #we merge their friend circles
                    if friend_circle != new_friend_circle:
                        merged_circle = friend_circle.mergeFriendCircle(new_friend_circle)
                        friend_circles.remove(friend_circle)
                        friend_circles.remove(new_friend_circle)
                        friend_circles.append(merged_circle)
                        
    return len(friend_circles)


friends = ['YYNN', 'YYYN', 'NYYN', 'NNNY']
print(friendCircles(friends))

friends = ['YNNNN', 'NYNNN', 'NNYNN', 'NNNYN','NNNNY']
print(friendCircles(friends))
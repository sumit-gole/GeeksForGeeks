#User function Template for python3

def isNeighbor(num):
    ##Your code here
    a = num % 10
    if  (10 - (10-a)) <= 2 or (10 - a) <= 2:
        return True
    else:
        return False

#User function Template for python3

def digitsSum(n):
    ##Your code here
    sum=0
    while(n>0):
        res=n%10
        sum+=res
        n=n//10
    return sum

#User function Template for python3

def doge_count(str):
    count=0
    for i in range(0,len(str)-3):
        if(str[i]=='d' and str[i+1]=='o' and str[i+3]=='e'):
            count+=1
    return count

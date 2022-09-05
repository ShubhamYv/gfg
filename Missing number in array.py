class Solution:
    def MissingNumber(self,array,n):
        # code here
        sum= int(n*(n+1)/2)
        for i in range(len(array)):
            sum= sum- array[i]
        return sum

class Solution:
    def firstNonRepeating(self, arr, n): 
        # Complete the function
        d={}
        for i in range(n):
            if arr[i] in d.keys():
                d[arr[i]]+=1
            else:
                d[arr[i]]=1
        for j in range(n):
            if d[arr[j]]==1:
                return arr[j]
        return -1

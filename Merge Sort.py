class Solution:
    def merge(self,arr, l, m, r): 
        # code here
        n1= m-l+1
        n2= r-m
        arr1= [0]*n1
        arr2= [0]*n2
        for i in range(n1):
            arr1[i]= arr[l+i]
        for i in range(n2):
            arr2[i]= arr[m+1+i]
        i=0
        j=0
        k=l
        while (i<n1 and j<n2):
            if arr1[i]< arr2[j]:
                arr[k]=arr1[i]
                k+=1
                i+=1
            else:
                arr[k]=arr2[j]
                k+=1
                j+=1
        while i<n1:
            arr[k] = arr1[i]
            k += 1
            i += 1
        while j<n2:
            arr[k] = arr2[j]
            k += 1
            j += 1
        return arr
        
    def mergeSort(self,arr, l, r):
        #code here
        if l<r:
            m= (r+l)//2
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m+1, r)
            self.merge(arr, l, m, r)



#{ 
 # Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends

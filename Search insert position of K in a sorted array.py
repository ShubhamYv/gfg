class Solution:
    def searchInsertK(self, Arr, N, k):
        # code here
        low=0
        high= N-1
        mid= 0
        while low<=high:
            mid=low+(high-low)//2
            if Arr[mid]== k:
                return mid
            elif Arr[mid]> k:
                high= mid-1
            else:
                low= mid+1
        return low

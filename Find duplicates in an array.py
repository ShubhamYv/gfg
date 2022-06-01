class Solution:
    def duplicates(self, arr, n): 
    	# code here
        n= len(arr)
    	dict= {}
        for i in range(0,n):
            if arr[i] in Map:
                dict[arr[i]]=dict[arr[i]]+1
            else:
                dict[arr[i]]=1
        result = [key for key, x in dict.items() if x>1]
        if result:
            result.sort()
            return result
        return [-1]

def main():
    t= int(input())
    for i in range(t):
        n= int(input())
        arr= list(map(int, input().split()))
        ob= Solution()
        ans= ob.duplicates(arr, n)
        print(ans)
        
if __name__ == '__main__':
    main()
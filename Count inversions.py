class Solution:
    def inversionCount(self, arr, n):
        count=0
        for i in range(0,n):
            for j in range(i+1,n):
                if arr[j]<arr[i]:
                    count+=1
        return count
    
def main():
    n= int(input())
    arr= list(map(int, input().split()))
    ob= Solution()
    ans= ob.inversionCount(arr, n)
    print(ans)
    
if __name__ == '__main__':
    main()
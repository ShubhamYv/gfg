class Solution:
    def minJumps(self, arr, n):
        n= len(arr)
        if n==1:
            return 0
        elif arr[0]== 0:
            return -1
        jumps, steps_possible, max_reach = 1, arr[0], arr[0]
        for i in range (1,n):
            if(i == n-1):
                return jumps
                
            max_reach = max(max_reach, i+arr[i])
            steps_possible-=1
            
            if(steps_possible == 0):
                jumps+=1
                if(i >= max_reach):
                    return -1
                steps_possible = max_reach - i
        
        return jumps
                
def main():
    t= int(input())
    for i in range(t):
        n= int(input())
        arr= list(map(int, input().split()))
        ob= Solution()
        ans= ob.minJumps(arr, n)
        print(ans)
        
if __name__ == "__main__":
    main()
    
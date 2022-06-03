class Solution:
    def majorityElement(self, A, N):
        d={}
        for x in A:
            try:
               d[x]+=1
            except:
               d[x]=1
        for x,y in d.items():
            if y>(N/2):
                return x
        return -1
    
def main():
    t= int(input())
    while t>0:
        N= int(input())
        A= list(map(int, input().split()))
        ob= Solution()
        res= ob.majorityElement(A, N)
        print(res)
        t-=1
        
if __name__ == '__main__':
    main()
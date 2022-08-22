class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        list=[]
        i=j=k=0
        while i<n1 and j< n2 and k<n3:
            if A[i]==B[j] and B[j]== C[k]:
                if A[i] not in list:
                    list.append(A[i])
                i+=1
                j+=1
                k+=1
                
            elif A[i]< B[j]:
                i+=1
            
            elif B[j]< C[k]:
                j+=1
                
            else:
                k+=1
        return list

#{ 
 # Driver Code Starts
#Initial Template for Python 3


t = int (input ())
for tc in range (t):
    n1, n2, n3 = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    ob = Solution()
    
    res = ob.commonElements (A, B, C, n1, n2, n3)
    
    if len (res) == 0:
        print (-1)
    else:
        for i in range (len (res)):
            print (res[i], end=" ")
        print ()

# } Driver Code Ends

class Solution:
    def isAnagram(self,a,b):
        #code here
        if len(a) != len(b):
            return False
        else:
            count = [0]*256
            for i in range(len(a)):
                count[ord(a[i])] +=1
                count[ord(b[i])] -=1
                
            if count == [0]*256:
                return True
            else: 
                return False
            
def main():
    ob= Solution()
    a= input()
    b= input()
    if(ob.isAnagram(a, b)):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()    
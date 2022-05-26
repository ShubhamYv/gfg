# def eleAppears(arr, n, k):
#     x= n//k
#     freq= {}
#     for i in range(n):
#         if arr[i] in freq:
#             freq[arr[i]]+=1
#         else:
#             freq[arr[i]]=1
#     for i in freq:
#         if freq[i]> x:
#             print(i, end= " ")
#     return

def eleAppears(arr, n, k):
    x= n//k
    freq= [0]*40
    for i in range(n):
        freq[arr[i]]+=1
    for i in range(40):
        if freq[i]> x:
            print(i, end=" ")
    return

def main():
    n= int(input())
    arr= list(map(int, input().split()))
    k= int(input())
    eleAppears(arr, n, k)

if __name__ == '__main__':
    main()
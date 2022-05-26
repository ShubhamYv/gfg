def rotate(arr, n):
    first= arr[n-1]
    for i in range(n-1, -1,-1):
        arr[i]= arr[i-1]
    arr[0]= first
    return arr


def main():
    n= int(input())
    arr= list(map(int, input().strip().split()))
    # print(arr)
    print(rotate(arr,n))

if __name__ == '__main__':
    main()
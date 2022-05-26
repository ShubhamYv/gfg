def longConsecutiveSubSeq(arr, n):
    arr.sort()
    count=1
    for i in range(n-1):
        if arr[i+1]- arr[i]==1:
            count+=1
        elif arr[i+1]- arr[i]==0:
            pass
    return count


def main():
    n= int(input())
    arr= list(map(int, input().split()))
    print(longConsecutiveSubSeq(arr, n))


if __name__ == '__main__':
    main()
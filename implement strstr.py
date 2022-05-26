def strstr(s,x):
    new_li = s.split(x)
    count = 0
    if len(new_li) == 1:
        return -1
    else:
        return len(new_li[0])

def main():
    s= input()
    x= input()
    print(strstr(s,x))

if __name__ == '__main__':
    main()

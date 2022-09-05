def getFloorAndCeil(arr, n, x):
    # code here
    floorArr=[]
    ceilArr=[]
    for i in arr:
        if i==x:
            floorArr.append(i)
            ceilArr.append(i)
        elif i>x:
            ceilArr.append(i)
        else:
            floorArr.append(i)
    if len(ceilArr)<1:
        return max(floorArr),-1
    elif len(floorArr)<1:
        return -1,min(ceilArr)
    else:
        return max(floorArr),min(ceilArr)

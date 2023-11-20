def moveZero(arr):
    size=len(arr)
    i=0
    j=0
    for j in range(size):
        if arr[j] != 0:
            temp=arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i=i+1
    return arr


arr=[1,2,3,0,2,0,1,1,0,2]
MArray=moveZero(arr)
for i in range(len(arr)):
    print(MArray[i], end= " ")
print()


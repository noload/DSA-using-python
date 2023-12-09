def pairSum(arr,target):
    left=0;
    right=len(arr) - 1;
    while(left<right):
        sum=arr[left] + arr[right]
        if(sum==target):
            return True
        elif(sum>target):
            right-=1;
        else:
            left+=1;
    return False

arr=[2,4,7,9,10]
target=13;
print(pairSum(arr,target))
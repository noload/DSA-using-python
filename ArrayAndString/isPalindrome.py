def is_Pallindrome(s):
    left=0;
    right=len(s) - 1;
    while(left<right):
        if(s[left]!=s[right]):
            return False
        left+=1
        right-=1
    return True

s="kamak"
ans = is_Pallindrome(s)
print(ans);
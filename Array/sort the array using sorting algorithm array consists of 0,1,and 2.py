class Solution:
    def sort012(self,arr,n):
        # code here
        c1 = 0
        c2 = 0
        c3 = 0
        for i in range(n):
            if arr[i]==0:
                c1+=1
            elif arr[i]==1:
                c2+=1
            elif arr[i]==2:
                c3+=1
        
        i = 0
        while c1>0:
                arr[i]=0
                i+=1
                c1-=1
        while c2>0:
                arr[i]=1
                i+=1
                c2-=1
        while c3>0:
                arr[i]=2
                i+=1
                c3-=1
        
        return arr
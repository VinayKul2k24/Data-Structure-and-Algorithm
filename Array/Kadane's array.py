  def maxSubArraySum(self,arr):
        curr_max = arr[0]
        maxx_so_far =arr[0]
        for i in range(1,len(arr)):
            curr_max=max(arr[i],curr_max+arr[i])
            maxx_so_far = max(maxx_so_far,curr_max)
        return maxx_so_far

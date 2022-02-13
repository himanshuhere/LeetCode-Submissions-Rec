class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #easily do with sorting thaty wud be nlogn but medium ques bnaya h bhai ku heap manje min heap use karo nlogk
        # O(k+(n-k)lgk) time, min-heap
        #1
        myheap = []
        for i in nums:
            heapq.heappush(myheap, i)
            if len(myheap) > k:
                heapq.heappop(myheap)     
        return heapq.heappop(myheap)
        
        #2 - better at interview - average time = o(n) / worst = o(n^2) very rare
        #QUICK SELECT  WOW, NICE
        
        
        def quickSelect(left, right, k):
            i = left
            pivot = nums[right]
            
            for j in range(left, right):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    
            nums[i], nums[right] = nums[right], nums[i]                     #do one swap of pivot and i'th
            
            count = right - i + 1                                           #number of ele greater than i
            if count < k:   
                return quickSelect(left, i-1, k - count)
            elif count > k: 
                return quickSelect(i+1, right, count)
            else:
                return nums[i]
        
        return quickSelect(0, len(nums)-1, k)
                

        
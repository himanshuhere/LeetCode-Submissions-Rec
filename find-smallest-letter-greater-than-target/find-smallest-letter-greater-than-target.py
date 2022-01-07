class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        #Find Smallest Letter Greater Than Target
        #find ceil of ele in sorted array, dont include ele fins greater than that
        #find the next char in sorted string or albhabets
        #binary search
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]
        
        
        
        lo = 0
        hi = len(letters)
        res = ""
        
        while lo <= hi:
            mid = lo + (hi - lo // 2)
            if letters[mid] < target:
                lo = mid + 1
            else:
                res = letters[mid]
                hi = mid - 1
        return res
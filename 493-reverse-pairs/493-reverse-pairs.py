class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        #Same problem - Count inversion pairs where a[i] > a[j] and i<j
        #Enhanced merge sort
        #Same merge sort, only one logic to count when my second right side array ele is smaller and we pick it, so that means every element after i to mid, is greater than my jth, so we count those as a[i], a[j] pair and ofc i<j as left and right arr
        cnt = 0

        def merge(left, right):
            nonlocal cnt
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= 2*right[j]:
                    i += 1
                else:
                    cnt += len(left)-i
                    j += 1

            return sorted(left+right)


        def mergeSort(A):
            if len(A) <= 1:
                return A
            return merge(mergeSort(A[:(len(A) + 1) // 2]), mergeSort(A[(len(A) + 1) // 2:]))

        mergeSort(nums)
        return cnt
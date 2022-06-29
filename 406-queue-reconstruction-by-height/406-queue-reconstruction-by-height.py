class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
#         Sort based on height in descending, and for persons with same height, sort in ascending based on k.
# Sorted Values:
# [[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]

# Then, construct queue with sorted list.

        result = []*len(people)
        people.sort(key = lambda a: (-a[0], a[1]))
        for x in people: 
            i = x[1]
            result.insert(i, x);
        return result
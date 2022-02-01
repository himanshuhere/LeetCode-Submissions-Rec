# set left and right bounds
left, right = 0, len(nums)-1
# left and right both converge to the minimum index;
# DO NOT use left <= right because that would loop forever
while left < right:
# find the middle value between the left and right bounds (their average);
# can equivalently do: mid = left + (right - left) // 2,
# if we are concerned left + right would cause overflow (which would occur
# if we are searching a massive array using a language like Java or C that has
# fixed size integer types)
mid = (left + right) // 2
# the main idea for our checks is to converge the left and right bounds on the start
# of the pivot, and never disqualify the index for a possible minimum value.
​
# in normal binary search, we have a target to match exactly,
# and would have a specific branch for if nums[mid] == target.
# we do not have a specific target here, so we just have simple if/else.
if nums[mid] > nums[right]:
# we KNOW the pivot must be to the right of the middle:
# if nums[mid] > nums[right], we KNOW that the
# pivot/minimum value must have occurred somewhere to the right
# of mid, which is why the values wrapped around and became smaller.
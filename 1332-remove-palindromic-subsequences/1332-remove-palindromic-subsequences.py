class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[::-1] else 2
    
    #That means, there are 3 situations of this problem:
        #1. String length equals 0 -> return 0;
        #2. String itself is a Palindrome -> return 1; (because you can remove them all at once)
        #3. Other cases, you can first remove all 'a' and then all 'b' or vice versa (first all 'b' then all 'a') -> return 2;
        
        #sare 'a' pakdo to palidrom hai nikal k feko 1 cost, sare b reh gye wo b palindrom hai cost =2, ab combination k bare me sochna hi nhi hai
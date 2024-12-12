class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        origialNumber = x
        reversedNumber = 0
        while x > 0:
            lastNumber = x%10
            reversedNumber = reversedNumber * 10 + lastNumber
            x = x // 10
        return reversedNumber == origialNumber
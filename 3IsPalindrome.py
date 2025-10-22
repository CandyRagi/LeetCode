# My solution
class Solution(object):    
    def isPalindrome(self,x):
        if(x<0):
            return False
        reversed=0
        original=x
        while(x!=0):        
            reversed=reversed*10+x%10
            x//=10
        if(reversed==original):
            return True    
        return False
    
# AI solution
class Solution(object):
    def isPalindrome(self, x):
        if x < 0: return False
        
        original, reversed = x, 0
        while original != 0:
            reversed = reversed * 10 + original % 10
            original //= 10
        return x == reversed
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        div = 1
        while x >= div*10:
            div *= 10
        while x:
            if x // div != x % 10:
                return False
            x = (x % div) // 10
            div = div // 100
        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        l, r = 0, len(s)-1
        while l < r:
            if ord(s[l]) < 97 and ord(s[l]) > 57 or ord(s[l]) < 48 or ord(s[l]) > 122:
                l += 1
            elif (ord(s[r]) < 97 and ord(s[r]) > 57 or  ord(s[r])< 48 or ord(s[r]) > 122):
                r -= 1
            elif (s[l] != s[r]):
                return False
            else:
                l += 1
                r -= 1
        return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1

        while i <= j:
            while (s[i].isalnum()) is False:
                i += 1
                if i > j:
                    return True

            while (s[j].isalnum()) is False:
                j -= 1
                if j < i:
                    return True

            if s[i].lower() != s[j].lower():
                return False

            print(i,j)
            i += 1
            j -= 1
        return True
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set_t = {}
        for char in t:
            if char in set_t:
                set_t[char] += 1
            else:
                set_t[char] = 1

        for char in s:
            if char in set_t:
                if set_t[char] > 0:
                    set_t[char] -= 1
                if set_t[char] == 0:
                    set_t.pop(char)
            else:
                return False

        return True


r = Solution()
print(r.isAnagram("anagram", "nagara"))

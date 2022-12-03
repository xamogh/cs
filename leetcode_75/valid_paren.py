import unittest
import pdb


class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {"{": "}", "(": ")", "[": "]"}
        stack = []

        if len(s) % 2 != 0:
            return False

        for idx, char in enumerate(s):
            if char == "{" or char == "(" or char == "[":
                stack.insert(0, char)

            else:
                if len(stack) == 0:
                    return False
                if bracket_map[stack[0]] == char:
                    stack.pop(0)
                else:
                    return False
        return True if len(stack) == 0 else False


class Test_valid_paren(unittest.TestCase):
    def test_isValid(self):
        self.assertEqual(Solution().isValid("()"), True)
        self.assertEqual(Solution().isValid("()[]{}"), True)
        self.assertEqual(Solution().isValid("(]"), False)
        self.assertEqual(Solution().isValid("){"), False)

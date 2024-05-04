from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        for i in range(len(knowledge)):
            s = s.replace('(' + knowledge[i][0] + ')', knowledge[i][1])

        i = 0
        while i < len(s):
            if s[i] == '(':
                j = i
                while s[j] != ')':
                    s = s[:i] + s[j + 1:]
                s = s[:i] + '?' + s[j + 1:]
            i += 1

        return s

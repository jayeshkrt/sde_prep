# https://leetcode.com/problems/minimum-window-substring/
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        window, countT = {}, {}

        for c in t:
            countT = 1 + countT.get(c, 0)

        have, required = 0, len(t)
        res, resLen = [-1,-1], float("infinity")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == required:
                # update our result
                if r-l+1 < resLen:
                    res, resLen = [l, r+1], r-l+1
                # pop from the left window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float('infinity') else ""


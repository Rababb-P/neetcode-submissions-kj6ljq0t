class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = {}
        max_count = 0
        left = 0
        for right in range(len(s)):
            if s[right] in char_set:
                left = max(left, char_set[s[right]] + 1)
            char_set[s[right]] = right
            max_count = max(max_count, right - left + 1)

        return max_count
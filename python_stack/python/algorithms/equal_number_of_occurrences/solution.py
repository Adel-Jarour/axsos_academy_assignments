class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        char_count = {}

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # counts = set(char_count.values())
        # return len(counts) == 1

        counts = list(char_count.values())
        return all(count == counts[0] for count in counts)
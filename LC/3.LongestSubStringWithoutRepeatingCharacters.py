class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        max_length = 0
        for x in range(len(s)):
            print(f"Processing character {s[x]} at index {x}")

            while s[x] in char_set:
                print(f"Character {s[x]} is already in char_set, removing {s[l]} from char_set")
                char_set.remove(s[l])
                l = l + 1
                print(f"Left pointer moved to index {l}")

            char_set.add(s[x])
            print(f"char_set after adding {s[x]}: {char_set}")

            max_length = max(max_length, x - l + 1)
            print(f"Updated max_length: {max_length}")

        return max_length


print(Solution().lengthOfLongestSubstring("abbabcdefa"))

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}

        for word in strs:
            n = ''.join(sorted(word))

            if n in anagram:
                anagram[n].append(word)
            else:
                anagram[n] = [word]

        return(list(anagram.values()))
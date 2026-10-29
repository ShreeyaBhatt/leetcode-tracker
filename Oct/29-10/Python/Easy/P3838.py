class Solution:
    def mapWordWeights(self, words, weights):
        ans = []
        for word in words:
            s = 0
            for c in word:
                s += weights[ord(c) - ord("a")]
            ans.append(chr(ord("z") - s % 26))
        return "".join(ans)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False

        CountS= {}
        CountT={}

        for ch in s:
            CountS[ch]=CountS.get(ch,0)+1
        for ch in t:
            CountT[ch]=CountT.get(ch,0)+1
        return CountS == CountT
        
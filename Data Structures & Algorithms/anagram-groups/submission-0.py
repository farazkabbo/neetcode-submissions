class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            sig = ''.join(sorted(s))   
            groups[sig].append(s)
        return list(groups.values())
        
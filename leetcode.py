class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ana={}
        for st in strs:
            sortstr=''.join(sorted(st))
            if sortstr in ana:
                ana[sortstr].append(st)
            else:
                ana[sortstr]=[st]
        return list(ana.values())
    
    
Solution.groupAnagrams(Solution,["eat","tea","tan","ate","nat","bat"])
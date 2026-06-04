# Group Anagrams

class Solution:
    
    def sortString(self,s):
        s = s.split()
        s.sort()
        print("hh","".join(s))
        return "".join(s)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}

        for s in strs:
            key = self.sortString(s)
            print(key)
            if key in dict1:
                dict1[key].append(s)
            else:
                dict1[key] = [s]

        return list(dict1.values())            


        
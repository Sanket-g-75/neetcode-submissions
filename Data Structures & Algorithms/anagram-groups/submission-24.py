class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anags = {}

        for i in strs:
            j = sorted(i)
            j = "".join(j)
            
            if j not in anags.keys():
                anags[j] = [i]
            else:
                anags[j].append(i)
        ans = [i for i in anags.values()]
        print(anags)
        return ans


        '''
        for i in strs:
            if i == "":
                anags.append(list('""'))
            else:
                new = []
                new.append(i)
                for j in strs:
                    if (i != j) and (sorted(i) == sorted(j)):
                        new.append(j)
                        continue
                print(sorted(new))
                if sorted(new) not in anags:
                    anags.append(sorted(new))
        return anags
        '''



    
                    
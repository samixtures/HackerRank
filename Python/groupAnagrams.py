class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        tempList = []
        map1 = {}
        map2 = {}
#         if x in map1: # looping through word eat
#             map1[x]+=1
#         else: map1[x] = 1
        index = 0
        tempStrs = list(strs)
        duplic = False

            
        for x in strs: # nat

            for l in range(len(result)):

                if x in result[l]:
                    duplic = True
                    break
                else: duplic = False
            if duplic == True: continue

            
            for y in x: # n nat
                if y in map1:
                    map1[y]+=1
                else: map1[y]=1
                #by the end map1 = e:1, a:1, t:1
   
            # strs.remove(x) #strs = - nat
            tempStrs.remove(x)
            for z in tempStrs: #nat
                for a in z: # a
                    if a in map2:
                        map2[a]+=1
                    else: map2[a]=1
                    #by the end map1 = t:1, e:1, a:1
                if map1 == map2:
                    tempList.append(z) #nat
                map2={}
                
                
            tempList.append(x) #tan, nat
            result.append(tempList)
            tempList=[]
            map1 = {}
            map2 = {}
            
            
        return result
            
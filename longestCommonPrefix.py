# My solution (Wrong)
class Solution(object):
    def longestCommonPrefix(self,strs):
        smallest_str=strs[0]
        temp=""
        for str in strs:
            if(len(smallest_str)>len(str)):
                smallest_str=str
                break
        for str in strs:
                for j in range (len(str)):
                     if(j+len(smallest_str)>len(str)):
                          break
                     if(str[j]==smallest_str[0]):
                          temp2=""
                          for i in range(len(smallest_str)):
                               if(smallest_str[i]==str[j+i]):
                                    temp2+=smallest_str[i]
                               else:
                                    break
                          if(len(temp)<len(temp2)):
                               temp=temp2

                smallest_str=temp
                if(smallest_str==""):
                     return ""

        return smallest_str
                          
# AI Solution
class Solution(object):
    def longestCommonPrefix(self,strs):
        if not strs: return ""
        smallest_str = min(strs, key=len)  # 1 line!
        
        for str in strs:
            if not str or not smallest_str: return ""
            # JUST CHECK START (j=0 only!)
            temp2 = ""
            for i in range(min(len(str), len(smallest_str))):
                if str[i] != smallest_str[i]: break
                temp2 += smallest_str[i]
            if len(temp2) < len(smallest_str):
                smallest_str = temp2
            if not smallest_str: return ""
        return smallest_str

            



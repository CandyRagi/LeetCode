# My Solution
class Solution(object):
    def isValid(self,str):
        paranthes={"{":"}","[":"]","(":")"}
        new_str=str
        for i in range(len(str)):
            for j in range(len(str)):
                if(paranthes[str[i]]==str[j]):
                    
                    if(j<len(str)-1):
                        new_str=new_str[:i]+new_str[i+1:j]+new_str[j:]
                    else:
                        new_str=new_str[:i]+new_str[i+1:j]


        if(new_str==""):
            return True
        
        return False


                        




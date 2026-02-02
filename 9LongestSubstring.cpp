#include<iostream>
#include<string>

using namespace std;

class Solution
{
    public:
        int lengthOfLongestSubstring(string s) {
        
        if(s.length()==0)
        {
            return 0;
        }
        if(s.length()==1)
        {
            return 1;
        }

        int i=0;
        int maxlength=0;
        while(i<s.length())
        {
            int appeared[128]={0};
            int local_max=1;
            appeared[s[i]]=1;
            for(int j=i+1;j<s.length();j++)
            {
                if(appeared[s[j]]==1)
                {   
                    if(local_max>maxlength)
                    {
                        maxlength=local_max;
                    }
                    break;
                }
                else
                {
                    appeared[s[j]]=1;
                    local_max+=1;
                }
            }

            if(local_max > maxlength)
            {
                maxlength = local_max;
            }

            i++;



        }

        return maxlength;
        
        
    }

};

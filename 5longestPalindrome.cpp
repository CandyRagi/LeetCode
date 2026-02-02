#include<iostream>
#include<string>

using namespace std;

class Solution
{
    public:

        string longestPalindrome(string s)
        {   
            if(s.length()==1)
            {
                return s;
            }
            auto isPalindrome=[](string s , int start,  int end)->bool
            {
                while(start<end)
                {
                if(s[start]!=s[end])
                {
                    return false;
                }
                start++;
                end--;
                }
                return true;
                
            };



            int start = 0;
            int end = s.length()-1;
            int lengthMax=1;
            int max=0;
            for(int i=0;i<end;i++)
            {
                for(int j=end;j>=i;j--)
                {
                    if(isPalindrome(s,i,j)==true)
                    {
                        if(lengthMax<j-i)
                        {
                            lengthMax=j-i;
                            max=i;
                        }
                    }
                    
                    
                }

            }
                
            string ret="";
            int i=max;
            while(i<=lengthMax)
            {
                ret=ret+s[i];
                i++;
            }

            return ret;

        }
};

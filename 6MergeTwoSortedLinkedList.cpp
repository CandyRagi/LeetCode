
struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode * i=nullptr;
        ListNode *j=nullptr;
        if(list1==nullptr && list2==nullptr)
        {
            return list1;

        }
        if(list1==nullptr)
        {
            return list2;

        }
        if(list2==nullptr)
        {
            return list1;

        }

        if(list1->val>list2->val)
        {
            i=list2;
            j=list1;
        }

        if(list1->val<=list2->val)
        {   
            i=list1;
            j=list2;
        }

        ListNode * sNode=nullptr;
        ListNode * sNode2=nullptr;

        while(j!=nullptr)
        {
            if((i->next)!=nullptr)
            {
            if(j->val<=(i->next)->val)
            {
                sNode=i->next;
                i->next=j;
                sNode2=j->next;
                j->next=sNode;
                j=sNode2;
                continue;
            }

            i=i->next;
            }
            else
            {i->next=j;
            break;
            }
        }

        if(list1->val>list2->val)
        {
            return list2;
        }
        return list1;

    }
};
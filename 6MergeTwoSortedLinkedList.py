class linked_List(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class solution(object):
    def mergeSortedLinkedList(self,list1,list2):

        if(list1 is None or list is None):
            return
            
        if(list1.val>list2.val):
            traverse=list2
            add=list1
        else:
            traverse=list1
            add=list2

        while(add!=None):
            while(traverse!=None):
                if(traverse.val>=add.val):
                    temp=add.next
                    add.next=list2
                    traverse=list2.next
                    list2.next=temp
                else:
                    add=add.next    

        return
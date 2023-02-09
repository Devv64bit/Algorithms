# Code by Dev Patel
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Standard base cases to check if list1 or list2 exists.
        if not list1:
            return list2

        if not list2:
            return list1

        list3 = ListNode()
        currentPtr = list3

        while list1 and list2:
            # Check if list1 value is lower list2 value
            # If true, add it to list3(temp)
            if list1.val < list2.val:
                currentPtr.next = list1
                list1 = list1.next

            # Vice Versa, add the values of list2 to list3(temp)
            else:
                currentPtr.next = list2
                list2 = list2.next

            # increment the currentPtr
            currentPtr = currentPtr.next

        # Add the remaining values of list1 and list2
        if list1:
            currentPtr.next = list1
        else:
            currentPtr.next = list2

        # return the sorted list stored in list3
        return list3.next

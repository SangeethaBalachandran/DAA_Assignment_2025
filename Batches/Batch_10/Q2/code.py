# LeetCode #23 — Merge K Sorted Lists
# Approach: Min Heap (Priority Queue)
# -----------------------------------

import heapq

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):   # ✅ corrected __init__
        self.val = val
        self.next = next

    # For easy printing of the linked list
    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)


# Function to merge K sorted linked lists
def mergeKLists(lists):
    heap = []

    # Step 1: Initialize the heap with the head node of each list
    for l in lists:
        if l:
            heapq.heappush(heap, (l.val, id(l), l))
            # id(l) ensures unique comparison even if values are same

    # Step 2: Create a dummy node to form the merged list
    head = point = ListNode(0)

    # Step 3: Extract the smallest node and push its next node
    while heap:
        val, _, node = heapq.heappop(heap)
        point.next = node
        point = point.next
        if node.next:
            heapq.heappush(heap, (node.next.val, id(node.next), node.next))

    return head.next


# Helper function to create linked lists from arrays
def build_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to convert list of arrays into linked lists
def build_list_of_linked_lists(list_of_arrays):
    return [build_linked_list(arr) for arr in list_of_arrays]


# -------------------------------
# Example Usage
if __name__ == "__main__":
    # Input: [[1,4,5], [1,3,4], [2,6]]
    lists = build_list_of_linked_lists([[1, 4, 5], [1, 3, 4], [2, 6]])

    # Merge all lists
    merged = mergeKLists(lists)

    # Print the merged linked list
    print("Merged Sorted Linked List:")
    print(merged)

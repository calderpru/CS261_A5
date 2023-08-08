# Name: Calder Prulhiere
# OSU Email: prulhiec@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 5
# Due Date: 7/8/2023
# Description: MinHeap Implementation


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """
        Adds a new object to the MinHeap while maintaining heap property.
        """
        self._heap.append(node)  # add new element to the end
        idx = self._heap.length() - 1  # index of the newly added element
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self._heap[idx] < self._heap[parent_idx]:  # if child < parent
                # swap
                self._heap[idx], self._heap[parent_idx] = self._heap[parent_idx], self._heap[idx]
                idx = parent_idx
            else:
                break

    def is_empty(self) -> bool:
        """
        Return True if the heap is empty, otherwise return False.
        """
        return self._heap.length() == 0

    def get_min(self) -> object:
        """
        Returns an object with the minimum key, without removing it from the heap.
        """
        if self.is_empty():
            raise MinHeapException("Heap is empty")
        return self._heap[0]


    def remove_min(self) -> object:
        """
        Returns an object with the minimum key, and removes it from the heap.
        """
        if self.is_empty():
            raise MinHeapException("Heap is empty")

        # If only one element, return it
        if self._heap.length() == 1:
            last_item = self._heap[0]
            self._heap.remove_at_index(0)
            return last_item

        # Store min value
        min_val = self._heap[0]
        # Move the last element to the root position
        last_item_index = self._heap.length() - 1
        self._heap[0] = self._heap[last_item_index]
        self._heap.remove_at_index(last_item_index)  # remove the last element
        _percolate_down(self._heap, 0, self._heap.length())

        return min_val

    def build_heap(self, da: DynamicArray) -> None:
        """
        Receives a DynamicArray with objects in any order and builds a MinHeap.
        """
        self._heap = DynamicArray()
        for i in range(da.length()):
            self._heap.append(da[i])

        for i in range(self._heap.length() // 2, -1, -1):
            _percolate_down(self._heap, i, self._heap.length())

    def _sift_down(self, idx):
        """
        Helper function for build_heap, to sift down the element at index idx.
        """
        child_idx = 2 * idx + 1
        while child_idx < self._heap.length():
            # If right child exists and is smaller than left child
            if child_idx + 1 < self._heap.length() and self._heap[child_idx + 1] < self._heap[child_idx]:
                child_idx += 1
            # If the current node is greater than its smallest child, swap them
            if self._heap[idx] > self._heap[child_idx]:
                # swap
                self._heap[idx], self._heap[child_idx] = self._heap[child_idx], self._heap[idx]
                idx = child_idx
                child_idx = 2 * idx + 1
            else:
                break

    def size(self) -> int:
        """
        Return the number of items in the heap.
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        Clear all items from the heap.
        """
        self._heap = DynamicArray()


def heapsort(da: DynamicArray) -> None:
    """
    Sort the given DynamicArray in-place using the heapsort algorithm.
    """

    # Turn the DynamicArray into a min heap.
    n = da.length()
    for i in range(n // 2 - 1, -1, -1):
        _percolate_down(da, i, n)

    # sort
    for i in range(n - 1, 0, -1):
        # Swap the smallest element with last element.
        da[i], da[0] = da[0], da[i]
        _percolate_down(da, 0, i)


# It's highly recommended that you implement the following optional          #
# function for percolating elements down the MinHeap. You can call           #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parent: int, size: int) -> None:
    """
    Helper function to percolate down from given index in a min heap.
    """
    left = 2 * parent + 1
    right = 2 * parent + 2
    smallest = parent

    if left < size and da[left] < da[smallest]:
        smallest = left
    if right < size and da[right] < da[smallest]:
        smallest = right
    if smallest != parent:
        da[parent], da[smallest] = da[smallest], da[parent]
        _percolate_down(da, smallest, size)
# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)

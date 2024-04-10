import collections
import heapq

def topKFrequent(nums, k):
    # Count the frequency of each number
    counter = collections.Counter(nums)
    
    # Create a min heap to store the top k frequent elements
    heap = []
    for num, freq in counter.items():
        if len(heap) < k:
            heapq.heappush(heap, (freq, num))
        else:
            # If heap is already of size k, push current element only if its frequency is higher than the lowest frequency in the heap
            if freq > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (freq, num))
    
    # Retrieve the top k frequent elements from the heap
    top_k_elements = [elem[1] for elem in heap]
    
    return top_k_elements


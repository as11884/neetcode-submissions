# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

from copy import copy

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        
        result = []
        if pairs:
            result.append(copy(pairs))
        for i in range(1, len(pairs)):
            key = pairs[i].key
            j = i - 1
            while(j >= 0 and pairs[j].key > pairs[j+1].key):
                temp = pairs[j]
                pairs[j] = pairs[j+1]
                pairs[j+1] = temp
                j -= 1
            result.append(copy(pairs))
        
        return result
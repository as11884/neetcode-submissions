class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.MergeSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def MergeSortHelper(self, pairs, start, end):
        if end - start <= 0:
            return pairs

        mid = (start + end) // 2

        self.MergeSortHelper(pairs, start, mid)
        self.MergeSortHelper(pairs, mid + 1, end)

        self.merge(pairs, start, mid, end)
        return pairs

    def merge(self, pairs, start, mid, end):
        leftpairs = pairs[start: mid + 1]
        rightpairs = pairs[mid + 1: end + 1]

        i = 0
        j = 0
        k = start
        while i < len(leftpairs) and j < len(rightpairs):
            if leftpairs[i].key <= rightpairs[j].key:
                pairs[k] = leftpairs[i]
                i += 1
            else:
                pairs[k] = rightpairs[j]
                j += 1
            k += 1
        
        while i < len(leftpairs):
            pairs[k] = leftpairs[i]
            k += 1
            i += 1

        while j < len(rightpairs):
            pairs[k] = rightpairs[j]
            k += 1
            j += 1
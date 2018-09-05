# -*- coding: utf-8 -*- 


class SearchAlgorithm:
    """docstring for SearchAlgorithm"""

    def __init__(self, L):
        self.L = L
        self.length = len(L)

    def SequentialSearch(self, k):
        """
        ASL = (n + 1) / 2
        """
        for i in range(self.length):
            if self.L[i] == k:
                return i
        return -1

    def BinSearch(self, k, start=0, end=None):
        """
        """
        if end is None:
            end = self.length - 1
        if end < start:
            return -1

        mid = (start + end) // 2
        if self.L[mid] > k:
            end = mid - 1
        elif self.L[mid] < k:
            start = mid + 1
        else:
            return mid
        return self.BinSearch(k, start, end)

if __name__ == "__main__":
    test_list = [2, 4, 3, 6, 33, 2, 7, 8, 9]
    test_list = sorted(test_list)
    sa = SearchAlgorithm(test_list)
    print(sa.BinSearch(7))
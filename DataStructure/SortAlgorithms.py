# -*- coding: utf-8 -*- 


class SortAlgorithm:
    """docstring for SortAlgorithm"""
    def __init__(self, L):
        self.L = L
        self.length = len(L)

    def swap(self, i, j):
        temp = self.L[i]
        self.L[i] = self.L[j]
        self.L[j] = temp


class ComparisonSort(SortAlgorithm):
    """docstring for ComparisonSort"""
    def __init__(self, L):
        super(ComparisonSort, self).__init__(L)

    def BubbleSort(self):
        """
        // 分类 -------------- 内部比较排序
        // 数据结构 ---------- 数组
        // 最差时间复杂度 ---- O(n^2)
        // 最优时间复杂度 ---- O(n)
        // 平均时间复杂度 ---- O(n^2)
        // 所需辅助空间 ------ O(1)
        // 稳定性 ------------ 稳定
        """
        for i in range(self.length - 1):
            for j in range(0, self.length - 1 - i):
                if self.L[j] > self.L[j + 1]:
                    self.swap(j, j + 1)

    def SelectionSort(self):
        pass

    def InsertionSort(self):
        for i in range(1, self.length):
            for j in range(0, i):
                if self.L[i] < self.L[j]:
                    for k in range(j, i, -1):
                        self.swap(k, k - 1)
                    print(self.L)
                    break


    def MergeSort(self):
        pass

    def QuickSort(self):
        pass

    def HeapSort(self):
        pass


if __name__ == "__main__":
    test_list = [2, 4, 3, 6, 33, 2, 7, 8, 9]
    cs = ComparisonSort(test_list)
    cs.InsertionSort()
    print(cs.L)
        
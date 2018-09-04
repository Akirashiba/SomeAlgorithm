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
        // 最差时间复杂度 ---- O()
        // 最优时间复杂度 ---- O()
        // 平均时间复杂度 ---- O()
        // 所需辅助空间 ------ O()
        // 稳定性 ------------ 
        """
        for i in range(self.length - 1):
            for j in range(0, self.length - 1 - i):
                if self.L[j] > self.L[j + 1]:
                    self.swap(j, j + 1)

    def SelectionSort(self):
        """
        // 分类 -------------- 内部比较排序
        // 数据结构 ---------- 数组
        // 最差时间复杂度 ---- O()
        // 最优时间复杂度 ---- O()
        // 平均时间复杂度 ---- O()
        // 所需辅助空间 ------ O()
        // 稳定性 ------------ 
        """
        for i in range(self.length - 1):
            k = i
            for j in range(i + 1, self.length):
                if self.L[j] < self.L[k]:
                    k = j
            if k != i:
                self.swap(i, k)

    def InsertionSort(self):
        """
        // 分类 -------------- 内部比较排序
        // 数据结构 ---------- 数组
        // 最差时间复杂度 ---- O()
        // 最优时间复杂度 ---- O()
        // 平均时间复杂度 ---- O()
        // 所需辅助空间 ------ O()
        // 稳定性 ------------ 
        """
        for i in range(1, self.length):
            for j in range(0, i):
                if self.L[i] < self.L[j]:
                    for k in range(i, j, -1):
                        self.swap(k, k - 1)
                    break


    def MergeSort(self):
        """
        // 分类 -------------- 内部比较排序
        // 数据结构 ---------- 数组
        // 最差时间复杂度 ---- O()
        // 最优时间复杂度 ---- O()
        // 平均时间复杂度 ---- O()
        // 所需辅助空间 ------ O()
        // 稳定性 ------------ 
        """
        pass

    def QuickSort(self, L):
        """
        // 分类 -------------- 内部比较排序
        // 数据结构 ---------- 数组
        // 最差时间复杂度 ---- O()
        // 最优时间复杂度 ---- O()
        // 平均时间复杂度 ---- O()
        // 所需辅助空间 ------ O()
        // 稳定性 ------------ 
        """
        i = 0
        j = len(L) - 1
        if len(L) > 1:
            k = L[i]
            while i < j:
                while L[j] >= k and i < j:
                    j -= 1
                L[i], L[j] = L[j], L[i]
                while L[i] <= k and i < j:
                    i += 1
                L[i], L[j] = L[j], L[i]
            return self.QuickSort(L[:i]) + [k] + self.QuickSort(L[i+1:])
        else:
            return L

    def HeapSort(self):
        pass


if __name__ == "__main__":
    test_list = [2, 4, 3, 6, 33, 2, 7, 8, 9]
    cs = ComparisonSort(test_list)
    print(cs.QuickSort(test_list))
    print(cs.L)
        
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
        // 最差时间复杂度 ---- O(n**2)  逆序
        // 最优时间复杂度 ---- O(n**2)  已排好序 O(n) Optimized
        // 平均时间复杂度 ---- O(n**2)
        // 所需辅助空间 ------ O(1)
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
        // 最差时间复杂度 ---- O(n**2)
        // 最优时间复杂度 ---- O(n**2)
        // 平均时间复杂度 ---- O(n**2)
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
        // 最差时间复杂度 ---- O(n**2) 逆序
        // 最优时间复杂度 ---- O(n)    已排好序
        // 平均时间复杂度 ---- O(n**2)
        // 所需辅助空间 ------ O(1)
        // 稳定性 ------------ 
        """
        for i in range(1, self.length):
            for j in range(0, i):
                if self.L[i] < self.L[j]:
                    for k in range(i, j, -1):
                        self.swap(k, k - 1)
                    break

    def MergeSortRecursive(self, L):
        """
        // 分类 -------------- 内部比较排序
        // 数据结构 ---------- 数组
        // 最差时间复杂度 ---- O()
        // 最优时间复杂度 ---- O()
        // 平均时间复杂度 ---- O()
        // 所需辅助空间 ------ O()
        // 稳定性 ------------ 
        """
        if len(L) > 1:
            left = self.MergeSortRecursive(L[:len(L) // 2])
            right = self.MergeSortRecursive(L[len(L) // 2:])
            k, i, j = 0, 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    L[k] = left[i]
                    i += 1
                else:
                    L[k] = right[j]
                    j += 1
                k += 1

            if i < len(left):
                for c in range(i, len(left)):
                    L[k] = left[c]
                    k += 1
            else:
                for c in range(j, len(right)):
                    L[k] = right[c]
                    k += 1
        return L

    def QuickSortRecursive(self, L):
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
            return self.QuickSortRecursive(L[:i]) + [k] + self.QuickSortRecursive(L[i+1:])
        else:
            return L

    def HeapSortRecursive(self, L):
        """
        // 分类 -------------- 内部比较排序
        // 数据结构 ---------- 数组
        // 最差时间复杂度 ---- O()
        // 最优时间复杂度 ---- O()
        // 平均时间复杂度 ---- O()
        // 所需辅助空间 ------ O()
        // 稳定性 ------------ 
        """
        if len(L) == 1:
            return L

        for i in range(len(L) // 2 - 1, -1, -1):
            leftleaf = i * 2 + 1
            rightleaf = i * 2 + 2
            if rightleaf < len(L) and L[rightleaf] > L[i]:
                L[rightleaf], L[i] = L[i], L[rightleaf]
            if leftleaf < len(L) and L[leftleaf] > L[i]:
                L[leftleaf], L[i] = L[i], L[leftleaf]

        L[0], L[-1] = L[-1], L[0]
        return self.HeapSortRecursive(L[:-1]) + [L[-1]]

    def ShellSort(self):
        pass

if __name__ == "__main__":
    test_list = [2, 4, 3, 6, 33, 2, 7, 8, 9]
    cs = ComparisonSort(test_list)
    print(cs.InsertionSort())
    print(cs.L)
        
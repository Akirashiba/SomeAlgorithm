# -*- coding: utf-8 -*-
import unittest
import random


def partition(array, head, tail):
    base = array[head]
    while head < tail:
        while head < tail and array[tail] >= base:
            tail -= 1
        array[head] = array[tail]
        while head < tail and array[head] <= base:
            head += 1
        array[tail] = array[head]
    array[head] = base
    return head


def quick_sort(array, head=None, tail=None):
    head = 0 if head is None else head
    tail = len(array) - 1 if tail is None else tail

    if head < tail:
        base = partition(array, head, tail)
        quick_sort(array, head, base-1)
        quick_sort(array, base+1, tail)

    return array


def merge_sort(array: list):
    if len(array) > 1:
        left = merge_sort(array[:len(array) // 2])
        right = merge_sort(array[len(array) // 2:])
        return merge(left, right)
    else:
        return array


def merge(array_left:list, array_right:list):
    result = []
    i, j = 0, 0
    while i < len(array_left) and j < len(array_right):
        if array_left[i] < array_right[j]:
            result.append(array_left[i])
            i += 1
        else:
            result.append(array_right[j])
            j += 1
    result.extend(array_left[i:])
    result.extend(array_right[j:])
    return result


def heapify(array, root_index, n=None):
    heap_size = len(array) if n is None else n

    lchild_index = root_index * 2 + 1
    rchild_index = root_index * 2 + 2

    largest = root_index
    if lchild_index < heap_size and array[lchild_index] > array[largest]:
        largest = lchild_index 
    if rchild_index < heap_size and array[rchild_index] > array[largest]:
        largest = rchild_index
    
    if largest != root_index:
        array[root_index], array[largest] = array[largest], array[root_index] 
        heapify(array, largest, heap_size)


def rank_score(score_list: list, max_score_limit: int):
    score_count = [0 for _ in range(max_score_limit+1)]
    for score in score_list:
        score_count[score] += 1
    rank_result = []
    for score, count in enumerate(score_count):  
        for _ in range(count):
            rank_result.append(score)
    return rank_result


class LinkNodeWithRandomPointer(object):
    
    def __init__(self, val, next_pointer=None, random_pointer=None, tag=None):
        if next_pointer:
            assert isinstance(next_pointer, self.__class__)
        if random_pointer:
            assert isinstance(random_pointer, self.__class__)
        self.random_pointer = random_pointer
        self.next_pointer = next_pointer
        self.val = val
        self.tag = tag

    def get_head_node_tuple(self):
        return (self.val, self.random_pointer.val if self.random_pointer else -1)

    def get_rest_of_link_list(self):
        link_list = []
        head_node = self
        while head_node is not None:
            link_list.append(head_node.get_head_node_tuple())
            head_node = head_node.next_pointer
        return link_list


def build_link_list_with_random_pointer(num_list: list):
    node_list = []
    for num in num_list:
        node_list.append(LinkNodeWithRandomPointer(num))
    
    total_length = len(node_list)
    for index, node in enumerate(node_list):
        if index + 1 < len(node_list):
            node.next_pointer = node_list[index+1]
        if random.randint(0, 1) == 1:
            random_index = random.randint(0, total_length-1)
            node.random_pointer = node_list[random_index] 

    return node_list[0] if node_list else None


def copy_link_list_with_random_pointer(head_node):
    origin_head_node = head_node
    while head_node is not None:
        copy_head_node = LinkNodeWithRandomPointer(head_node.val)
        next_node = head_node.next_pointer
        head_node.next_pointer = copy_head_node
        copy_head_node.next_pointer = next_node
        head_node = next_node

    head_node = origin_head_node
    while head_node is not None:
        next_head_node = head_node.next_pointer.next_pointer
        copy_node = head_node.next_pointer
        if head_node.random_pointer:
            copy_node.random_pointer = head_node.random_pointer.next_pointer
        head_node = next_head_node
    
    copy_head_node = origin_head_node.next_pointer
    copy_node = origin_head_node.next_pointer
    while copy_node is not None:
        if copy_node.next_pointer:
            next_node = copy_node.next_pointer.next_pointer
            copy_node.next_pointer = copy_node.next_pointer.next_pointer
        else:
            next_node = None
        copy_node = next_node

    return copy_head_node



class NormalLinkNode:

    def __init__(self, val):
        self.val = val
        self.next_pointer = None

    def get_rest_of_link_list(self):
        head_node = self
        link_list = []
        while head_node is not None:
            link_list.append(head_node.val)
            head_node = head_node.next_pointer
        return link_list


def build_normal_link_list(num_list):
    if not num_list:
        return None
    head_node = NormalLinkNode(num_list[0])
    cur_node = head_node
    for num in num_list[1:]:
        cur_node.next_pointer = NormalLinkNode(num)
        cur_node = cur_node.next_pointer
    return head_node


def bubble_sort_link_list(head_node):
    last_node = None
    cur_node = head_node
    while cur_node is not last_node:
        while cur_node.next_pointer is not last_node:
            if cur_node.val > cur_node.next_pointer.val:
                temp = cur_node.val
                cur_node.val = cur_node.next_pointer.val
                cur_node.next_pointer.val = temp 
            cur_node = cur_node.next_pointer 
        last_node = cur_node
        cur_node = head_node
    return head_node


def merge_sort_link_list(head_node):
    if head_node is None or head_node.next_pointer is None:
        return head_node
    quick_cur = head_node
    slow_cur = head_node
    mid_cur = head_node
    while quick_cur and quick_cur.next_pointer:
        mid_cur = slow_cur
        slow_cur = slow_cur.next_pointer
        quick_cur = quick_cur.next_pointer.next_pointer
    left_head_node = head_node
    right_head_node = mid_cur.next_pointer
    mid_cur.next_pointer = None
    left = merge_sort_link_list(left_head_node)
    right = merge_sort_link_list(right_head_node)
    return merge_link_list(left, right)


def merge_link_list(left_head_node, right_head_node):
    pre_head = NormalLinkNode(-1)
    
    cur_node = pre_head
    while left_head_node and right_head_node:
        if left_head_node.val < right_head_node.val:
            cur_node.next_pointer = left_head_node
            left_head_node = left_head_node.next_pointer
        else:
            cur_node.next_pointer = right_head_node
            right_head_node = right_head_node.next_pointer
        cur_node = cur_node.next_pointer

    if left_head_node:
        cur_node.next_pointer = left_head_node
    else:
        cur_node.next_pointer = right_head_node
    
    return pre_head.next_pointer


class BinaryTreeNode(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_binary_tree(num_list: list):
    node_list = []
    for i in range(len(num_list)):
        node = BinaryTreeNode(num_list[i], None, None)
        node_list.append(node)

    if node_list:
        for i in range(len(num_list) // 2 - 1):
            left_child_index = i*2 + 1
            right_child_index = i*2 + 2 
            if left_child_index < len(num_list):
                node_list[i].left = node_list[left_child_index]
            if right_child_index < len(num_list):
                node_list[i].right = node_list[right_child_index]   

    return node_list[0]


class TestAlgorithm(unittest.TestCase):

    def setUp(self):
        print("test start")

    # def test_quicksort(self):
    #     test_set = [3, 44, 34, 53, 624, 452, 4235, 7, 13, 52, 41, 1, 16]
    #     sorted_test_set = sorted(test_set)
    #     quick_sort(test_set)
    #     self.assertEqual(test_set, sorted_test_set)

    # def test_merge_sort(self):
    #     test_set = [3, 44, 34, 53, 624, 452, 4235, 7, 13, 52, 41, 1, 16]
    #     sorted_test_set = sorted(test_set)
    #     test_set = merge_sort(test_set)
    #     self.assertEqual(test_set, sorted_test_set)

    # def test_heapify(self):
    #     test_set = [3, 44, 34, 53, 624, 452, 4235, 7, 13, 52, 41, 1, 16]
    #     sorted_test_set = sorted(test_set)
    #     for root_index in range(len(test_set)//2 - 1, -1, -1):
    #         heapify(test_set, root_index)
    #     for heap_size in range(len(test_set)-1, 0, -1):
    #         test_set[heap_size], test_set[0] = test_set[0], test_set[heap_size] # swap 
    #         heapify(test_set, 0, heap_size)
    #     self.assertEqual(test_set, sorted_test_set)

    # def test_rank_score(self):
    #     import random
    #     max_score_limit = 750
    #     test_set = [random.randint(0, 750) for _ in range(100000)]
    #     sorted_test_set = sorted(test_set)
    #     ranked_score_list = rank_score(test_set, max_score_limit)
    #     self.assertEqual(ranked_score_list, sorted_test_set)

    # def test_build_link_list_with_random_pointer(self):
    #     test_set = [1, 3, 2, 5, 32, 53, 22, 11]
    #     head_node = build_link_list_with_random_pointer(test_set)
    #     link_list = head_node.get_rest_of_link_list()
    #     self.assertEqual(test_set, [_[0] for _ in link_list])

    # def test_copy_link_list_with_random_pointer(self):
    #     test_set = [1, 3, 2, 5, 32, 53, 22, 11]
    #     head_node = build_link_list_with_random_pointer(test_set)
    #     link_list = head_node.get_rest_of_link_list()
    #     copy_head_node = copy_link_list_with_random_pointer(head_node)
    #     copy_link_list = copy_head_node.get_rest_of_link_list()
    #     self.assertEqual(link_list, copy_link_list)

    # def test_build_normal_link_list(self):
    #     test_set = [1, 3, 2, 5, 32, 53, 22, 11]
    #     head_node = build_normal_link_list(test_set)
    #     link_list = head_node.get_rest_of_link_list()
    #     self.assertEqual(test_set, link_list)

    # def test_bubble_sort_link_list(self):
    #     test_set = [1, 3, 2, 5, 32, 53, 22, 11]
    #     head_node = build_normal_link_list(test_set)
    #     link_list = head_node.get_rest_of_link_list()
    #     sorted_link_list = sorted(link_list)
    #     sorted_head_node = bubble_sort_link_list(head_node)
    #     _link_list = sorted_head_node.get_rest_of_link_list()
        
    #     self.assertEqual(_link_list, sorted_link_list)

    def test_merge_sort_link_list(self):
        test_set = [1, 3, 2, 5, 32, 53, 22, 11]
        head_node = build_normal_link_list(test_set)
        link_list = head_node.get_rest_of_link_list()
        sorted_link_list = sorted(link_list)
        sorted_head_node = merge_sort_link_list(head_node)
        _link_list = sorted_head_node.get_rest_of_link_list()
        
        self.assertEqual(_link_list, sorted_link_list)



if __name__ == "__main__":
    unittest.main()

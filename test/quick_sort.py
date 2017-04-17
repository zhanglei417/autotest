#!/usr/bin/python
# -*- coding: UTF-8 -*-


L = [3,4,5,1,2]


def quick_sort(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        # 如果右面元素大于等于左面key元素则减一位继续判断
        while left < right and lists[right] >= key:
            right -= 1
        # 发现有小于最左面key元素的右面元素后将其赋给左面第一个元素
        lists[left] = lists[right]
        # 如果左面元素小于等于左面key元素则加一位继续判断
        while left < right and lists[left] <= key:
            left += 1
        # 发现有大于最左面key元素的左面元素后将其赋给右面刚才判断的赋值给左面元素的元素
        lists[right] = lists[left]
        print "---- 一轮排序 ----"
        print L
        print "---- 一轮排序 ----"
    # 循环判断直到左右都判断完毕
    # 将key赋值给加完的或者减完的元素，完成一轮二分，就是将比key小的放在左面。比key大的放在右面
    lists[left] = key
    print "----排序后----"
    print L
    print "----排序后----"
    # 再去递归排序
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists


def bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


def insert_sort(lists):
    # 插入排序
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        # 插入排序，最后一个数插入到前面的数列，如果最后一个数小于前面遍历的数，那么前面遍历的数就和后面的数互换。
        # 如果最后一个数大于前面的数就不变了，因为前面的数已经便利完毕，从第一第二个数开始遍历。后面往前插入。
        # 前面的数列是顺序排好的，所以如果插入的话肯定是一个一个从后往前换
        while j >= 0:
            if lists[j] > key:
                lists[j+1] = lists[j]
                lists[j] = key
            j -= 1
    return lists



# print quick_sort(L,0,4)
# print bubble_sort(L)
print insert_sort(L)
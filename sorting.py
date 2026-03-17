# sorting.py
# 实现冒泡排序算法
def bubble_sort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # 最后 i 个元素已经有序，不需要再比较
        for j in range(0, n - i - 1):
            # 如果当前元素大于下一个元素，交换位置
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 测试代码
if __name__ == "__main__":
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bubble_sort(test_arr)
    print("排序后的数组:", sorted_arr)

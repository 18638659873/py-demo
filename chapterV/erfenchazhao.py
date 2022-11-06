# 需要查到的集合，二分查找必须是有序的
lst = [2, 5, 6, 9, 11, 15, 35, 55, 66, 99]

n = int(input("请输入需要查找的数字"))

lIdx = 0

rIdx = len(lst) - 1

while rIdx >= lIdx:
    midIdx = (rIdx + lIdx) // 2
    if n > lst[midIdx]:
        lIdx = midIdx + 1
    elif n < lst[midIdx]:
        rIdx = midIdx - 1
    else:
        print("找到了：" + lst[midIdx])
else:
    print("没有找到")

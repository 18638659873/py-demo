# 创建一个迷宫
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 设置起点
start = (1, 1)
# 设置终点
end = (8, 8)

lst = [start]

while lst:
    now = lst[-1]
    row, col = now
    maze[row][col] = 2
    if now == end:
        print(lst)
        print("exit")
        break
    if maze[row - 1][col] == 0:
        lst.append((row - 1, col))
        continue
    elif maze[row][col - 1] == 0:
        lst.append((row, col - 1))
        continue
    elif maze[row + 1][col] == 0:
        lst.append((row + 1, col))
        continue
    elif maze[row][col + 1] == 0:
        lst.append((row, col + 1))
        continue
    else:
        lst.pop()
else:
    print("over")

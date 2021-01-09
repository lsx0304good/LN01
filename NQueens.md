## N 皇后问题

在棋盘中，皇后可以攻击同一行、同一列，或者左上、左下、右上、右下四个方向的任意单位。现在有一个 N x N 的棋盘，请放置 N 个皇后，使她们不能互相攻击，返回所有合法的结果。

### 分析问题：

- 首先解决 N 皇后问题的本质是就是 **决策树的遍历**，或者说是 **多叉树的遍历**，也就是 **回溯问题**

- 对于回溯问题，我们需要考虑三个要素：

  1. 路径：在决策树中已经做过的选择
  2. 选择列表：在当前节点所面临的选择
  3. 结束条件：到达了决策树的最底层，没有更多选择

- 回溯算法的框架如下：

  ```python
  result = []
  def backtrack(path, choices):
      # trigger to terminate
      if meetRequirement():
          result.append(path)
          return
      # core framework
      for choice in choices:
          makeChoice()
          backtrack(path, choices)
          undoChoice()
  ```

  - 在框架中，`makeChoice()`是前序遍历，发生在递归之前；相同的，`undoChoice()`为后序遍历，发生在递归之后
  - 我们需要在做决策之前先考虑这个选择是否符合要求，例如避免重复的路径
  - **前序遍历自顶之下，后序遍历自底至上**
  - 在递归之后撤销选择的原因是 **维护每个节点的选择列表和路径** (choices and path)
  - 回溯算法的特点是穷举整个决策树，所以 **时间复杂度不可能低于 O(N!)**

### 解决 N 皇后问题：

```python
# create a board
def createBoard(n):
    board = []
    for _ in range(n):
        board.append(['.'] * n)
    return board


def backtrack(board, row):
    # trigger to terminate
    if row == len(board):
        # print out result
        # for i in board:
        #     print(i)
        # print('\n')
        return board
    n = len(board[row])
    for col in range(n):
        if not isValid(board, row, col):
            continue
        # core algorithm
        board[row][col] = 'Q'
        backtrack(board, row + 1)
        board[row][col] = '.'

# check if the position meets requirement
def isValid(board, row, col):
    n = len(board)
    for i in range(row):
        if board[i][col] == 'Q':
            return False
	
    # check top right
    tmp_row = row - 1
    tmp_col = col + 1
    while tmp_row >= 0 and tmp_col < n:
        if board[tmp_row][tmp_col] == 'Q':
            return False
        tmp_row -= 1
        tmp_col += 1
	
    # check top left
    tmp_row = row - 1
    tmp_col = col - 1
    while tmp_row >= 0 and tmp_col >= 0:
        if board[tmp_row][tmp_col] == 'Q':
            return False
        tmp_row -= 1
        tmp_col -= 1

    return True


if __name__ == '__main__':
    board_size = int(input("please enter the size of board:"))
    board = createBoard(board_size)
    backtrack(board, 0)
```

- 在这里我们要注意的是 `isValid()`函数起到了 “**剪枝**” 的作用，由于在**放置 Q 时顺序是从上向下，所以在检查 “X” 相邻时，只需考虑左上和右上**
- 在递归中，对于每一行的每一列检查，最终返回满足条件的解，然后撤销这次放置，还原选择以便 for loop 的下一步操作



## 举一反三 - 全排列问题

将 n 个不重复数字进行全排列，列出所有情况

### 思路：

- 根据上述 N 皇后问题，这道题依旧是回溯问题，所以框架仍然适用
- 全排列的本质就是选择在选择列表和路径之前的 add 和 remove
- 在递归前从选择列表中拿出一个选择放进路径中，**此步骤为前序遍历，从 parent node 到 child node**
- 为了维护每个 node 的选择列表和路径，**递归后需要把选择从路径放回至选择列表**，**此步骤为后序遍历，从 child node 到 parent node**
- 考虑一个结束条件，**也就是没有选择的情况**
- 考虑一个舍弃条件，**也就是选择需要符合的条件**

```python
def backtrack(nums, trackList):
    if len(trackList) == len(nums):
        print(trackList)
        return
    for i in nums:
        if i in trackList:
            continue
        # 前序进行选择
        trackList.append(i)
        # 递归
        backtrack(nums, trackList)
        # 后序维护选择列表
        trackList.pop()

if __name__ == '__main__':
    trackList = []
    nums = [1, 2, 3]
    backtrack(nums, trackList)

# result:
'''
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
'''
```
## 广度优先搜索

区别广度优先搜索（Board First Search）与深度优先搜索（Depth First Search）

- 广度优先的本质就是从一个图中找出起点到终点的最短距离，深度优先也就是回溯算法
- 广度优先是扩散性的，从一个点扩散到周围相邻的点，每一步都向周边扩散一次；深度优先是递归，一条路走到头，穷举出所有可能的结果。换句话说，**广度优先是面，深度优先是线。**
- 广度优先的 **空间复杂度高于** 深度优先
- **一般在找最短距离的时候使用广度优先**，其他情况使用深度优先

### 联想记忆：

从数学角度讲，两点之间线段最短，但在终点未知的情况下，最好的方法就是以起点为圆心画圆，半径从0开始递增，直至圆的轨迹覆盖了终点，此时半径即为最短距离

Broad First Search 中 Broad 一词可联想到 Broadcast，抽象起来也是从中心的信号塔向周边广播，直到终点接收到信号

### 算法框架：

- 这里需要用到 Queue 数据结构

- 另一个容器 visited 来 **保存已经走过的节点**，避免重复搜索

- 在进入循环之前，需要把 **起点** 加入到队列中

- 每个节点在 **进入队列的同时，也需要被记录到 visited 中**

  ```python
  def BFS(start, end):
      queue = Myqueue()
      visited = set()
      
      # initialization
      queue.push(start)
      visited.add(start)
      step = 0
      
      while not queue.empty():
          for i in range(len(queue)):
              current_node = queue.pop()
              if current_node is target:
                  return step
              for node in current_node.adj(): # adjacent nodes of current_node
                  if node not in visited:
                      queue.push(node)
                      visited.add(node)
          step += 1
  ```

## 

### 使用框架：二叉树的最小高度

这个问题在广度优先的框架上进行了修改，目的是求一个二叉树的最小高度，也就是**从 root 到一个没有子节点的节点的最短距离**

```java
int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        int depth = 1;

        while (!q.isEmpty()) {
            int sz = q.size();
            for (int i=0; i<sz; i++) {
                TreeNode cur = q.poll();
                if (cur.left == null && cur.right == null) {
                    return depth;
                }

                if (cur.left != null){
                    q.offer(cur.left);
                }

                if (cur.right != null){
                    q.offer(cur.right);
                }

                depth ++;
            }
            return depth;
        }
        return depth;
    }
```



### 加深难度：揭开密码锁的最少次数

一个四位密码锁，从 0000 转到 目标密码的最少次数

`deadends` 代表 **不可以** 拨到的密码

### 思路：

- 首先确定拨密码的两种情况：**向上** 和 **向下**
- 0000 为起点，开始向下扩散，当拨 **一次** 的时候会出现 **8** 种情况（4 向上，4 向下）
- 每次拨完一种情况，将其加入到 queue 和 visited 中，并且将其父节点从 queue 中移除

```java
public String plusOne(String s, int j) {
        char[] ch = s.toCharArray();

        if (ch[j] == '9') {
            ch[j] = '0';
        }
        else {
            ch[j] += 1;
        }

        return new String(ch);
    }

    public String minusOne(String s, int j) {
        char[] ch = s.toCharArray();

        if (ch[j] == '0') {
            ch[j] = '9';
        }
        else {
            ch[j] -= 1;
        }

        return new String(ch);
    }

    public int openLock(String[] deadends, String target) {
        Set<String> deads = new HashSet<>(Arrays.asList(deadends));

        Set<String> visited = new HashSet<>();
        Queue<String> q = new LinkedList<>();

        int step = 0;
        q.offer("0000");
        visited.add("0000");

        while (!q.isEmpty()) {
            int sz = q.size();
            for (int i = 0; i < sz; i++) {
                String cur = q.poll();

                if (deads.contains(cur)) {
                    continue;
                }

                assert cur != null;
                if (cur.equals(target)) {
                    return step;
                }

                for (int j = 0; j < 4; j++) {
                    String up = plusOne(cur, j);
                    if (!visited.contains(up)) {
                        q.offer(up);
                        visited.add(up);
                    }

                    String down = minusOne(cur, j);
                    if (!visited.contains(up)) {
                        q.offer(down);
                        visited.add(down);
                    }
                }
            }
            step++;
        }
        return -1;
    }
```


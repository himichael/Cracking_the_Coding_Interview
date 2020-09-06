class Solution(object):
    def solveNQueens(self, n):
        # 创建一个N行的数组，下标i对应N*N棋盘格子第i行的皇后位置
        arr = [-1 for _ in xrange(n)]
        # 三个集合，分别判断某一列，左斜线(左上到右下的斜线)，右斜线(左下到右上的斜线)
        columns = set()
        hypotenuse1 = set()
        hypotenuse2 = set()
        res = []
        def dfs(x):
            if x==n:
                # 如果x==n说明所有的皇后都摆放完了
                # 将arr数组中保存的结果拼接起来
                tmp = []
                row = ["."]*n
                for k in xrange(n):
                    row[arr[k]] = "Q"
                    tmp.append("".join(row))
                    row[arr[k]] = "."
                res.append(tmp)
                return
            # 遍历一行中的每一列，并检查竖线、左斜线、右斜线是否有皇后    
            for y in xrange(n):
                if y in columns:
                    continue
                if x-y in hypotenuse1:
                    continue
                if x+y in hypotenuse2:
                    continue
                # 如果检查通过，设置这一行的皇后位置，并将竖线、左斜线、右斜线的值放入集合中，并继续下一行递归    
                # 当下一层的所有递归遍历完后，回到本轮需要将之前集合、arr数组中保存的结果都清空
                arr[x] = y
                columns.add(y)
                hypotenuse1.add(x-y)
                hypotenuse2.add(x+y)
                dfs(x+1)
                arr[x] = -1
                columns.remove(y)
                hypotenuse1.remove(x-y)
                hypotenuse2.remove(x+y)
        dfs(0)
        return res
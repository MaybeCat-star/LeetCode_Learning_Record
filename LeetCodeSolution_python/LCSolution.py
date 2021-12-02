from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        all = sum(nums)
        left = 0
        for i in range(len(nums)):
            if left * 2 + nums[i] == all:
                return i
            else:
                left += nums[i]
        return -1    


    def searchInsert(self, nums: List[int], target: int) -> int:
        b = len(nums)-1
        a = 0
        while a <= b:
            i = (a + b) // 2
            if target == nums[i]:
                return i
            elif target < nums[i]:
                b = i - 1
            else:
                a = i + 1
        return a


    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


    def rotateMatrix(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        a, b = [], []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    a.append(i)
                    b.append(j)
        for k in range(len(a)):
            for i in range(m):
                matrix[i][b[k]] = 0
            for j in range(n):
                matrix[a[k]][j] = 0


    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        m = len(mat)
        n = len(mat[0])
        a = []
        for k in range(m+n-1):
            if k % 2 == 0:
                if k < m:
                    i = k
                    j = 0
                else:
                    i = m - 1
                    j = k - i
                while 0 <= i and j <= n-1:
                    a.append(mat[i][j])
                    i -= 1
                    j += 1                    
            else:
                if k < n:
                    j = k
                    i = 0
                else:
                    j = n - 1
                    i = k - j
                while 0 <= j and i <= m-1:
                    a.append(mat[i][j])
                    i += 1
                    j -= 1
        return a


    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = lambda i:len(i),reverse=False)
        b = len(strs[0])
        n = len(strs)
        if n == 1:
            return strs[0]
        for i in range(b):
            for j in range(n):
                if strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]


    def reverseWords(self, s: str) -> str:
        tmp = ''
        re = ''
        a = 0
        for i in range(len(s)):
            if s[i] == ' ':
                if s[i-1] == ' ':
                    a = i
                else:
                    tmp = s[a:i]
                    a = i
                    tmp = tmp.strip()
                    re = tmp + ' ' + re
            if i == len(s)-1:
                tmp = s[a:]
                re = tmp + ' ' + re
        re = re.strip()
        return re
        # return (' ').join(reverse(s.split())
        # 看了答案发现居然只需要这一行代码。


    def strStr(self, haystack: str, needle: str) -> int:
        a = len(needle)
        b = len(haystack)
        if needle == '':
            return 0
        for i in range(b-a+1):
            if haystack[i:i+a] == needle:
                return i
        return -1
        # 暴力匹配，尚未实现不匹配时跳过（continue）


    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        # s, i = 0, 0
        # while i < len(nums):
        #     s += nums[i]
        #     i += 2
        # return s
        return sum(nums[::2])


    def twoSumForSorted(self, numbers: List[int], target: int) -> List[int]:
        a, b = 0, len(numbers)-1
        while a < b:
            if target == numbers[a] + numbers[b]:
                ans = [a+1, b+1]
                return ans
            elif target > numbers[a] + numbers[b]:
                a += 1
            else:
                b -= 1


    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
    

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = count = 0

        for num in nums:
            if num == 1:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 0
        
        maxCount = max(maxCount, count)
        return maxCount


    def generate(self, numRows: int) -> List[List[int]]:
    # 输出前n行杨辉三角
        ans = []
        for i in range(1, numRows+1):
            ans.append([1] * i)
            for j in range(1, i-1):
                ans[i-1][j] = ans[i-2][j-1] + ans[i-2][j] 
        return ans
    # 思路没有问题，但是测试运行时间更长，以下是官方题解：
    # def generate(self, numRows: int) -> List[List[int]]:
    #     ret = list()
    #     for i in range(numRows):
    #         row = list()
    #         for j in range(0, i + 1):
    #             if j == 0 or j == i:
    #                 row.append(1)
    #             else:
    #                 row.append(ret[i - 1][j] + ret[i - 1][j - 1])
    #         ret.append(row)
    #     return ret


    def getRow(self, rowIndex: int) -> List[int]:
    # 输出第n行杨辉三角
        row = [0] * (rowIndex+1)
        row[0] = 1
        for i in range(1, rowIndex+1):
            for j in range(i, 0, -1):
                row[j] += row[j - 1]
        return row


    def rotateList(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k:] + nums[:n - k]


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[0] * 9 for _ in range(9)]
        col = [[0] * 9 for _ in range(9)] 
        box = [[0] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                curNum = ord(board[i][j]) - ord('1')
                if row[i][curNum] != 0 or col[j][curNum] != 0 or box[j // 3 + (i // 3) * 3][curNum] != 0:
                    return False
                row[i][curNum], col[j][curNum], box[j // 3 + (i // 3) * 3][curNum] = 1, 1, 1
        return True


    # 翻转整数，我的代码：
    def reverse(self, x: int) -> int:
        ans = 0
        tmp = x
        count = 0
        n = 1
        if x < 0:
            n *= -1
            x *= -1
            tmp *= -1
        while tmp // 10 != 0:
            count += 1
            tmp //= 10
        while count >= 0:
            ans += (x % 10) * (10 ** count)
            x //= 10
            count -= 1
        if ans > 2 ** 31 - 1 or ans < 2 ** -31:
            return 0
        return ans * n
    # 官方题解：
    # def reverse(self, x: int) -> int:
    #     INT_MIN, INT_MAX = -2**31, 2**31 - 1

    #     rev = 0
    #     while x != 0:
    #         # INT_MIN 也是一个负数，不能写成 rev < INT_MIN // 10
    #         if rev < INT_MIN // 10 + 1 or rev > INT_MAX // 10:
    #             return 0
    #         digit = x % 10
    #         # Python3 的取模运算在 x 为负数时也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
    #         if x < 0 and digit > 0:
    #             digit -= 10

    #         # 同理，Python3 的整数除法在 x 为负数时会向下（更小的负数）取整，因此不能写成 x //= 10
    #         x = (x - digit) // 10
    #         rev = rev * 10 + digit
        
    #     return rev   


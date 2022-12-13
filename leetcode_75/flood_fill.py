

from typing import List


class Queue:
    def __init__(self) -> None:
        self.q = []

    def push(self, value):
        self.q.append(value)
        return self.q[len(self.q) - 1]

    def get(self):
        return self.q.pop(0)

    def isEmpty(self):
        return len(self.q) == 0


class Solution:
    def floodFill(self, img: List[List[int]], row: int, column: int, color: int) -> List[List[int]]:
        if img[row][column] == color:
            return img
        queue = Queue()
        queue.push((row, column))
        prev_color = img[row][column]

        while not queue.isEmpty():
            (r, c) = queue.get()
            if r < 0 or r >= len(img) or c < 0 or c >= len(img[0]) or prev_color != img[r][c]:
                continue
            else:
                img[r][c] = color
                queue.push((r + 1, c))
                queue.push((r - 1, c))
                queue.push((r, c + 1))
                queue.push((r, c - 1))

        return img


r = Solution()
r.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)

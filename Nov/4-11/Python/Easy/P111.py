from collections import deque

class Solution:
    def minDepth(self, root):
        if root is None:
            return 0

        queue = deque([root])
        minLevel = 1

        while queue:
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()

                if node.left is None and node.right is None:
                    return minLevel

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            minLevel += 1

        return minLevel
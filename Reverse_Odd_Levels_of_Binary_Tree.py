# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Queue for BFS
        queue = collections.deque([root])
        level = 0 

        while queue:
            level_size = len(queue)
            # this array wil store nodes on the level
            curr_level_nodes = []

            for i in range(level_size):
                # Collect nodes at the current level
                node = queue.popleft()
                curr_level_nodes.append(node)
                # append child nodes into the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Reverse the values of nodes at odd levels
            if level % 2 == 1:
                # Collect the values
                values = [node.val for node in curr_level_nodes]
                # reverse the values
                values.reverse()

                # Assign the reversed values back to the nodes
                for i in range(level_size):
                    curr_level_nodes[i].val = values[i]

            # Move to the next level
            level += 1

        return root    

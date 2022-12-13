# class Node:
#     def __init__(self, value, left, right) -> None:
#         self.value = value
#         self.left = left
#         self.right = right


# class BST:
#     def __init__(self) -> None:
#         self.root = Node(0, None, None)

#     def add(self, value):
#         root = self.root
#         parent_node = self.root
#         while root:
#             if value > self.root:
#                 root = root.right
#             else:
#                 root = root.left
#             parent_node = root
#         if value > parent_node:
#             parent_node.right = Node(value, None, None)
#         else:
#             parent_node.left = Node(value, None, None)
#         self.root.value += 1

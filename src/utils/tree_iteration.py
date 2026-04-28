class TreeNode:
    def __init__(self, value):
        self.value = value
        
    def add_child(self,child_node):
        self.children.append(child_node)
        
class TreeIterator:
    def __init__(self, root):
        self.stack = [root]
    def __iter__(self):
        return self
    def __next__(self):
        if not self.stack:
            raise StopIteration
        current_node = self.stack.pop()
        self.stack.extend(reversed(current_node.children))
        return current_node.value

if __name__ == "__main__":
    root = TreeNode(1)
    root.add_child(TreeNode(2))
    root.add_child(TreeNode(3))
    root.children[0].add_child(TreeNode(4))
    root.children[0].add_child(TreeNode(5))
    root.children[1].add_child(TreeNode(6))
    root.children[1].add_child(TreeNode(7))

    iterator = TreeIterator(root)
    for value in iterator:
        print(value)
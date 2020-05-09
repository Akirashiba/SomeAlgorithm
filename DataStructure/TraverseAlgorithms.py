class TreeNode:
    def __init__(self, x):
        self.val = x
        self.lchild = None
        self.rchild = None

class TreeTraversal:

    @classmethod
    def preorder_traversal_recursive(cls, root):
        # 先序遍历递归版本
        if root is None:
            return []
        return [root.val] + \
            cls.inorder_traversal_recursive(root.lchild) + \
            cls.inorder_traversal_recursive(root.rchild)

    @classmethod
    def inorder_traversal_recursive(cls, root):
        # 中序遍历递归版本
        if root is None:
            return []
        return \
            cls.preorder_traversal_recursive(root.lchild) + \
            [root.val] + \
            cls.preorder_traversal_recursive(root.rchild) 

    @classmethod
    def postorder_traversal_recursive(cls, root):
        # 后序遍历递归版本
        if root is None:
            return []
        return \
            cls.inorder_traversal_recursive(root.lchild) + \
            cls.inorder_traversal_recursive(root.rchild) + \
            [root.val]
    
    @classmethod
    def preorder_traversal_iteratively(cls, root):
        # 前序遍历非递归版本
        if root is None:
            return []
        stack, result = [], []
        stack.append(root)
        while stack:
            cur_root = stack.pop()
            result.append(cur_root.val)
            
            if cur_root.right:
                stack.append(cur_root.right)

            if cur_root.left:
                stack.append(cur_root.left)

    @classmethod
    def inorder_traversal_iteratively(cls, root):
        # 中序遍历非递归版本
        stack, result = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                stackNode = stack.pop()
                result.append(stackNode.val)
                root = stackNode.right
        return result

    @classmethod
    def postorder_traversal_iteratively(cls, root):
        # 后序遍历非递归版本
        result = []
        if root is None:
            return result
        stack1 = [root]
        stack2 = []

        while stack1:
            cur_root = stack1.pop()
            stack2.append(cur_root)
            if cur_root.left:
                stack1.append(cur_root.left)
            if cur_root.right:
                stack1.append(cur_root.right)
        
        while stack2:
            cur_root = stack2.pop()
            result.append(cur_root.val)


if __name__ == "__main__":
    TreeTraversal()    

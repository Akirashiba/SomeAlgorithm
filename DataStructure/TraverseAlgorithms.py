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
        # 算法思想: 不用递归也只能用堆栈来代替了
        # 前序遍历 先右后左压栈
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
        # 算法思想: 一直往左孩子走 遇到的结点压栈
        # 左孩子没有就往右孩子走
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
        # 算法思想:
        stack, result = [], []


if __name__ == "__main__":
    TreeTraversal()    

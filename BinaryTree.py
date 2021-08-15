import collections

class Tree():
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None
    
    def add_num(self, num):
        #Parameters: Integer to be added 
        #Return: None
        if not self.root:
            self.root = Tree(num)
            return
        while True:
            if self.root == num: #BSTs only store unique values
                break
            if self.root < num:
                if self.right is None:
                    self.right = Tree(num)
                    return
                else:
                    self = self.right
            else:
                if self.left is None:
                    self.left = Tree(num)
                    return
                else:
                    self = self.left
    
    def add_multiple_nums(self, nums):
        #Parameters: list of nums
        #Return: None
        for num in nums:
            self.add_num(num)
        
    def minimum(self):
        #Parameters: None
        #Returns: the smallest integer
        while self.left:
            self = self.left
        return self.root
    
    def maximum(self):
        #Parameters: None
        #Returns: the largest integer
        while self.right:
            self = self.right
        return self.root
    
    def find_successor(self, num):
        if not self.search_for_element(num):
            return None
        def helper(node, low, high):
            if num == node.root:
                if node.right:
                    temp = node.right
                    while temp.left:
                        temp = temp.left
                    return temp.root
                return high if high > num else None
            elif num > node.root:
                node = node.right
                return helper(node, low, node.root)
            else:
                node = node.left
                return helper(node, node.root, high)
        return helper(self, self.root, self.root)  

    def find_predecessor(self, num):
        if not self.search_for_element(num):
            return None
        def helper(node, low, high):
            if num == high:
                if node.left:
                    return node.left.root
                else:
                    return low if low < num else None
            elif num > node.root:
                node = node.right
                return helper(node, high, node.root)
            else:
                node = node.left
                return helper(node, low, node.root)
        return helper(self, self.root, self.root)

    def search_for_element(self, num):
        #Parameters: Element to be searched for (int)
        #Return: if the element isn't found, False is returned. Otherwise, the node itself is returned. 
        node = self
        while True:
            if node.root == num:
                return node
            elif node.root > num:
                if node.left is None:
                    return False
                else:
                    node = node.left
            else:
                if node.right is None:
                    return False
                else:
                    node = node.right
        return False
    
    def inorder_traversal(self):
        #Parameters: None
        #Return: list of integers sorted based on in-order traversal of the tree
        nums = []    
        def inorder_helper(node):
            if node:
                inorder_helper(node.left)
                nums.append(node.root)
                inorder_helper(node.right)
        
        inorder_helper(self)        
        return nums

    
    def preorder_traversal(self):
        #Parameters: None
        #Return: list of integers sorted based on pre-order traversal of the tree
        nums = []
        def preorder_helper(node):
            if node:
                nums.append(node.root)
                preorder_helper(node.left)
                preorder_helper(node.right)
        
        preorder_helper(self)      
        return nums
    
    def postorder_traversal(self):
        #Parameters: None
        #Return: list of integers sorted based on post-order traversal of the tree
        nums = []
        def postorder_helper(node):
            if node:
                postorder_helper(node.left)
                postorder_helper(node.right)
                nums.append(node.root)
        
        postorder_helper(self)      
        return nums
    
    def levelOrder_traversal(self):
        #Parameters: None
        #Return: A list of lists of integers sorted from left to right at each level in the binary tree. 
        nums = []
        q = collections.deque()
        q.append(self)
        while q:
            temp = []
            for i in range(len(q)):
                node = q.popleft()
                temp.append(node.root)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            nums.append(temp)
        return nums
    
    def height_balanced_tree(self):
        nums = self.inorder_traversal()

        def helper(low, high):
            if low <= high:
                mid = (low + high) // 2
                node = Tree(nums[mid])
                node.left = helper(low, mid-1)
                node.right = helper(mid+1, high)
                return node
            else:
                return None
        
        self = helper(0, len(nums)-1)
        return self.levelOrder_traversal()

    def get_size(self):
        #Parameters: None
        #Return: Size of BST
        return len(self.inorder_traversal())
    
    def depth(self):
        #Parameters: None
        #Return: max depth 
        def helper(node):
            if not node:
                return 0
            else:
                return 1 + max(helper(node.left), helper(node.right))
        return helper(self)
    
    def lowestCommonAncestor(self, num1, num2):
        #Parameters: two integers 
        #Return: the lowest common ancestor
        if not self.search_for_element(num1) or not self.search_for_element(num2):
            return False
        while self:
            if num1 < self.root and num2 > self.root or num1 > self.root and num2 < self.root or self.root == num1 or self.root == num2:
                return self.root
            elif num1 > self.root and num2 > self.root:
                self = self.right
            else:
                self = self.left
    
    def remove(self, num):
        #Parameters: integer to be removed
        #Return: Bool
        node = self.search_for_element(num)
        if not node:
            return False
        if not node.left and not node.right:
            node = None
            return True
        
        
    

            
            


    
Tree1 = Tree(3)
Tree1.add_num(4)
Tree1.add_num(-5)
Tree1.add_num(4)
Tree1.add_num(0)
Tree1.add_multiple_nums([2,6,8,-3, 10, 12, 15, 16])
print(Tree1.find_predecessor(-3))
# print(Tree1.height_balanced_tree())
# print(Tree1.lowestCommonAncestor(12,-1))
# print(Tree1.levelOrder_traversal())

    
    
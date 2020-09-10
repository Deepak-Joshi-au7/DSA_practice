class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

#Time Complexity: O(N), Space Complexity: O(N)
def BT_BranchSums(root):
    sums = []
    calculateBT_BranchSums(root,0,sums)
    return sums

def calculateBT_BranchSums(node,runningSum,sums):
    if node is None:
        return

    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    calculateBT_BranchSums(node.left, newRunningSum,sums)
    calculateBT_BranchSums(node.right,newRunningSum,sums)

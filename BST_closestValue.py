# Average : time complexity: O(log(n)) | space complexity: O(Log(n))
# Worst: time complexity: O(n) | Space Complexity: O(n)

def findClosestValueInBst(tree,target):
    return findClosestValueInBstHelper(tree, target);

def findClosestValueInBstHelper(tree,target,closest):
    if tree is None:
        return closest;
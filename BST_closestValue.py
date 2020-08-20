# Average : time complexity: O(log(n)) | space complexity: O(Log(n))
# Worst: time complexity: O(n) | Space Complexity: O(n)

def findClosestValueInBst(tree,target):
    return findClosestValueInBstHelper(tree, target,float("inf"))

def findClosestValueInBstHelper(tree,target,closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left,target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right,target, closest)
    else :
        return closest

# Average : time complexity: O(log(n)) | space complexity: O(1)
# Worst: time complexity: O(n) | Space Complexity: O(1)

# tierative method without recursion

def findClosestValueInBst1(tree,target):
    return findClosestValueInBstHelper(tree, target,float("inf"))

def findClosestValueInBstHelper1(tree,target,closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - tree.value):
            closest = currentNode.value
        if target < tree.value:
            currentNode = currentNode.left
        elif target > tree.value:
            currentNode = currentNode.right
        else :
            break
    return closest

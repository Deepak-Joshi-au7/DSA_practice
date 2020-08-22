#Time Complexity = O(N) || Space Complexity = O(N)

#Solution 1
# Time Complexity = O(N^2) || Space Complexity = O(1)
def twoNumberSum(array,targetSum):
    for i in range(len(array)-1):
        firstNum = array[i]
        for j in range(i+1,len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum,secondNum]
    return []


#Solution 2
# Time Complexity = O(N) || Space Complexity = O(n)
def twoNumberSum1(array,targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if targetSum in nums:
            return [targetSum - num,num]
        else:
            nums[num] = True
    return []

#Solution 3
# Time Complexity = O(nlog(n)) || Space Complexity = O(1)
def twoNumberSum2(array,targetSum):
    array.sort()
    left = 0
    right = len(array) -1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return [] 
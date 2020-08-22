#Time Complexity = O(N) || Space Complexity = O(N)

def twoNumberSum(array,targetSum):
    for i in range(len(array)=1):
        firstNum = array[i]
        for j in range(i+1,len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetNum:
                return [firstNum,secondNum]
    return [];
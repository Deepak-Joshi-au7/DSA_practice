# Time Complexity = O(n)
# Space Complexity = O(1)


#Solution 1 (using while loop)
# Worst case Complexity (can be less than O(N))
# Time Complexity = O(N) || Space Complexity = O(1) 
def validateSubsequence(array,sequence):
    arrPP = 0
    seqPP = 0
    while arrPP < len(array) and seqPP < len(sequence):
        if array[arrPP] == sequence[seqPP]:
            seqPP += 1
        arrPP +=1
    return seqPP == len(sequence)

#Solution 2 (using for loop)
# Worst case Complexity (can be less than O(n))
# Time Complexity = O(N) || Space Complexity = O(1)
def validateSubsequence1(array,sequence):
    seqPP = 0
    for  value in array:
        if seqPP == len(sequence):
            break
        if sequence[seqPP] == value:
            seqPP +1
    return seqPP == len(sequence)
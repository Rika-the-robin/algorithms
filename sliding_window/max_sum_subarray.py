'''
Maximum Sum Subarray of Size K (easy)
Problem Statement
Given an array of positive numbers and a positive number ‘k,’ find the maximum
sum of any contiguous subarray of size ‘k’.
'''

def maxsum_subarray(array,k):
    result = []
    maxsum = 0
    tempsum = 0
    start = 0
    for idx in range(len(array)):
        tempsum += array[idx]
        print tempsum
        if idx >= k-1:
            print "idx",idx
            if tempsum > maxsum:
                maxsum = tempsum
                result = array[start:idx+1]
                print result
            tempsum -= arr[start]
            start +=1
    return result

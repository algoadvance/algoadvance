---
layout: page
title: Two sum
permalink: /l1-two-sum
---

[AlgoAdvance Blog](https://algoadvance.github.io/algoadvance)

[AlgoAdvance](https://algoadvance.com)


Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


### Clarifying Questions 
1. **Are all the elements in the input array distinct?** - Although we are given that there is exactly one solution, this does not necessarily imply that all elements are distinct. The presence of duplicate numbers (as in Example 3) should be taken into account. 
2. **What should be the behavior if the input array is empty or contains fewer than two elements?** - Since the problem guarantees exactly one solution, we can assume the input constraints allow for at least two elements. 
3. **Can the input array contain negative numbers?** - There is no restriction provided that limits the values to positive integers. Understanding these clarifications ensures we design an algorithm that meets the problem constraints effectively.

### Strategy 
To solve this problem efficiently, we can use a hashmap (or dictionary in Python) to store the elements of the array and their corresponding indices as we iterate through the array. 1. **Initialize an empty dictionary to keep track of the numbers and their indices.** 2. **Iterate through each element in the array.** - For the current element, calculate the required complement that, when added to the current element, equals the target. - Check if this complement is already present in the dictionary. - If the complement is found, return the indices of the current element and the complement. - If the complement is not found, add the current element along with its index to the dictionary and proceed to the next element. 

### Code 
def two_sum(nums, target): # Dictionary to hold the number and its index num_dict = {} # Iterate over the array for index, num in enumerate(nums): # Determine the needed complement complement = target - num # Check if complement exists in the dictionary if complement in num_dict: # Return the indices of the current number and the complement return [num_dict[complement], index] # Store the number and its index in the dictionary num_dict[num] = index # Test cases print(two_sum([2, 7, 11, 15], 9)) # Output: [0, 1] print(two_sum([3, 2, 4], 6)) # Output: [1, 2] print(two_sum([3, 3], 6)) # Output: [0, 1] "
(string)

### Time Complexity 
The time complexity of the above solution is \(O(n)\), where \(n\) is the number of elements in the array. This is because we perform a single traversal of the array, and dictionary operations (insert and lookup) are \(O(1)\) on average.
### Space Complexity 
The space complexity is also \(O(n)\) because, in the worst case, we might need to store all \(n\) elements in the dictionary."

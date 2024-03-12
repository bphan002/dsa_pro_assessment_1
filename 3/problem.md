# Max Weight on Shelves

Imagine you have `n` storage shelves labeled from `0` to `n-1`, each with specified weight capacities in the `capacity` array and the current number of items in the `items` array. Additionally, there is an integer called `additionalItems` representing the surplus items available for distribution.

Determine the maximum number of shelves that can reach their full capacity by distributing the extra items among the shelves.

## **Example 1:**
```
Input: capacity = [2,4,7,9], items = [1,1,5,0], additionalItems = 3
Output: 2
Explanation: You can add 2 items to the third bag to make it full, and one marble to the first bag, resulting in two bags at full capacity.
```

## **Example 2:**
```
Input: capacity = [3,5,7], items = [3,5,7], additionalItems = 5
Output: 3
Explanation: All 3 bags are already at capacity. No additionalItems necessary.
```
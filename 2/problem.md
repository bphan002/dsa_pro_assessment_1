# Data Processing

You are managing a computer network and need to determine the contiguous sets of servers that can collectively process a specified `target` amount of data. Given a list of `data_processing_capacity`, where `data_processing_capacity[i]` represents the capacity of the `ith` server, and a `target` amount of data to process, create a function that returns the minimum number of server sets needed to meet or exceed the target data processing capacity. If no such solution exists, return `0`.

## **Example 1:**
```
Input: target = 10, data_processing_capacity = [2,3,6,2,5,1]
Output: 3
Explanation: The shortest number of contiguous servers where we can reach 10 units is 3. One way is with servers from index 1 to 3.
```

## **Example 2:**
```
Input: target = 3, data_processing_capacity = [5,1,3]
Output: 1
Explanation: We can reach the target with a single server (servers at index 0 or 2).
```
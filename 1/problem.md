# Locate a Book by ISBN

You are provided with a sorted list of `book_ISBNs` in ascending order, represented as integers. Your goal is to efficiently locate a particular book. Develop a function that enables you to swiftly search for the given `ISBN`, returning its index if it exists or -1 if it does not.

Ensure that your algorithm is effective even for extensive sets of book ISBNs.

## **Example 1:**
```
Input: book_ISBNs = [2, 4, 6, 8, 10], ISBN = 8
Output: 3
```

## **Example 2:**
```
Input: book_ISBNs = [3, 5, 7, 9, 15], ISBN = 10
Output: -1
```
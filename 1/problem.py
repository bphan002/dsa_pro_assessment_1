class Solution:
    def locateBook(self, book_ISBNs, ISBN):
        # Remove pass and write code here
        left = 0
        right = len(book_ISBNs) - 1
        
        while left < right:
            mid = left + (right-left)//2
            print('mid',mid)
            if book_ISBNs[mid] == ISBN:
                return mid
            elif book_ISBNs[mid] > ISBN:
                right = mid - 1
            else:
                left = mid + 1

        return -1
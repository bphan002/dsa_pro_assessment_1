class Solution:
    def maxWeight(self, capacity, items, additionalItems):
        # subtract items from capacity
        #will overwrite capacity list to save on space
        #loop through capacity again and if additional item is still greater than or equal to 0
        #that means 
        for i in range(len(items)):
            capacity[i] -= items[i]

        capacity.sort()  
        full_shelf = 0

        for empty_spot in capacity:
            additionalItems -= empty_spot
            if additionalItems >= 0:
                full_shelf +=1
            if additionalItems <=0:
                return full_shelf
            
        return full_shelf

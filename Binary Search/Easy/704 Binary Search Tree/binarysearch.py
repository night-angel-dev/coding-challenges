def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    
    
    # So we are being given an integer list nums.
    # We want to search for integer target.
    
    # Based on the examples the list is already sorted.
    
    # Slicing an array in python would create a new copy of an array, making both the 
    # time and space complexity O(n). So we have to cross that out of our options.
    
    # Instead of a recursive function, we will use a while loop
    # while left is less than or equal to right. This will ensure left and right variables won't pass each other.
    # set a middle element by setting variable equal to (left + right) // 2
    
    # We will check cases in which middle variable is less than target
    #   if yes set left to middle + 1
    # if middle variable is greater than target
    #   if true set right to middle - 1
    # else
    #   we found the middle index and should be returned
    
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        
        middle = (left + right) // 2 # Set middle to middle index of array using floor division on size of array by 2
        
        if nums[middle] < target:
            
            left = middle + 1
            
        elif nums[middle] > target:
            
            right = middle - 1
            
        else:
            return middle
        
        
    # if the above does not return target's index, then return -1 
    # to indicate target is not in the list 
    return -1
    

# Lets test out the above function

# Array of size 10 with target 
arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Array being used {arr1}")
print(search(arr1, 1)) # should return 1
print("\n")

# Array of size 10 without target
arr2 = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10]
print(f"Array being used {arr2}")
print(search(arr2, 7)) # should return - 1
print("\n")


        
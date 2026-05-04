
def twoSum_bruteForce(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    # Given integer array nums
    # And an integer target

    # Return indices of the two numbers such that they add up to target
        
    # Brute force:

    # For i = 0; i < n ; i++

    for i in range(0, len(nums) ):

        # for j = i + 1 ; j < n ; j ++

        print(i)

        for j in range(i + 1, len(nums) ):

            print(j)

            # if arr[i] + arr[j] = target

            if (nums[i] + nums[j]) == target:

                return [i , j ]

                # return [i, j]
                

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
               
    # Version less than O(n^2) time complexity

    # Iterate through the list and input it into a hash map

    seen = {}

    # O(n)
    for i in range(0, len(nums)):
        
        element = nums[i]

        if element not in seen:
        
            seen[element] = i
    
    # O(n)

    # For each number calculate what complmenet we need to to reach the target
    for i in range(0, len(nums)):

        complement = target - nums[i]

        # Look up if we ahve already seen that complement

        if (complement in seen) and (i != seen[complement]):

            return [seen[complement], i]

    return []

    # Total time complexity = O(n) + O(n) = O(2n) not O(n^2)
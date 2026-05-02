
class BinarySearch {

    public int search(int[] nums, int target) {

        // Same logic as in binarysearch.py
        /*
            # Instead of a recursive function, we will use a while loop
            # while left is less than or equal to right. This will ensure left and right variables won't pass each other.
            # set a middle element by setting variable equal to (left + right) // 2
            
            # We will check cases in which middle variable is less than target
            #   if yes set left to middle + 1
            # if middle variable is greater than target
            #   if true set right to middle - 1
            # else
            #   we found the middle index and should be returned
        */
        
        // Initialize left and right index variables
        int left = 0;
        int right = nums.length - 1;
        
        while (left <= right) {

            int middle = (left + right) / 2; // Integer by integer division in hava is same as floor division in python

            if (nums[middle] < target) {
                left = middle + 1;
            }

            else if (nums[middle] > target) {
                right = middle - 1;
            }

            else {
                return middle;
            }

        }

        // Target is not in array return -1 
        return -1;

    }

    // Main
    public static void main(String[] args) {
        // Kind of left this empty, got too lazy. Only tested on leetecode.
    }

}
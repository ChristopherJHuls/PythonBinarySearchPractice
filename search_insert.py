import random

#target = 3
target = random.randint(0,20)
nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print('Target: ' + str(target))
print('Nums: ' + str(nums))

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left = 0
    right = len(nums) - 1
    loop_counter = 1

    print('Left Index at Start: ' + str(left))
    print('Right Index at Start: ' + str(right))
    print(' ')
    print(' ')
    
    while left <= right:
        mid = left + (right - left) // 2

        print('Loop Number: ' + str(loop_counter))
        print('Searching for ' + str (target) + ' in: ' + str(nums[left:right + 1]))
        print('Left Index: ' + str(left))
        print('Right Index: ' + str(right))
        print('Mid Index (left + (right - left)/2): ' + str(mid))
        print(' ')
        print(' ')
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            print(str(target) + ' is larger than ' + str(nums[mid]) + '. Set left bound to ' + str(nums[mid + 1]) + '. (Index = ' + str(mid + 1) + ')')
            print(' ') 
            print(' ')
            left = mid + 1
        else:
            print(str(target) + ' is smaller than ' + str(nums[mid]) + '. Set right bound to ' + str(nums[mid - 1]) + '. (Index = ' + str(mid - 1) + ')')
            print(' ')
            print(' ')
            right = mid - 1

        loop_counter += 1
    
    print(str(target) + ' is not in nums. Its index would be: ')
    return left
    #Left index is returned because if the target is not in the array, left > right and loop will stop. The left index is where the target should have been so we return it. 
    

print(search(nums, target))

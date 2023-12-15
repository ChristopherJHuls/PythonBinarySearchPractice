import random

#target = 3
target = random.randint(0,9)
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

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

    print('Left Start: ' + str(left))
    print('Right Start: ' + str(right))
    print(' ')
    print(' ')
    
    while left <= right:
        mid = left + (right - left) // 2

        print('Loop Number: ' + str(loop_counter))
        print('Searching in: ' + str(nums[left:right + 1]))
        print('Left: ' + str(left))
        print('Right: ' + str(right))
        print('Mid (left + (right - left)/2): ' + str(mid))
        print(' ')
        print(' ')
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            print(str(target) + ' is larger than ' + str(mid) + '. Set left bound to ' + str(mid + 1))
            print(' ') 
            print(' ')
            left = mid + 1
        else:
            print(str(target) + ' is smaller than ' + str(mid) + '. Set right bound to ' + str(mid - 1))
            print(' ')
            print(' ')
            right = mid - 1

        loop_counter += 1
    
    return -1

print(search(nums, target))

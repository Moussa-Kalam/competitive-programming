testcase = int(input())

for _ in range(testcase):
    n = int(input())
    nums = input().split()
    
    num_count = dict()

    for num in nums:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    
    print(num_count)

    # unique_nums = set(nums)

    # for element in nums:
    #     if len(nums) != len(unique_nums) and num_count[element] > 1:
    #         nums.remove(element)

    start_index = 0
    end_index = len(nums) - 1
    print("before", len(nums))

    while start_index < end_index:
        if num_count[nums[start_index]] > 1:
            nums.remove(nums[start_index])
            num_count[nums[start_index]] -= 1
        start_index = 0

        # if num_count[nums[end_index - 1]] > 1:
        #     nums.remove(nums[end_index - 1])
        #     num_count[nums[end_index - 1]] -= 1
        # end_index -= 1
    print("after", len(nums))



[2, 2, 2, 3, 3, 3]


    # if count of element is 1, do not remove
    # else remove one
    # check the count again
    
    # for the second element to remove, the count > 1
    # else do not remove it
        
    # Make it a set
    # compare the length of set and array
    # if the lengths are not equal 
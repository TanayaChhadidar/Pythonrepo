def highestOccurringElement(nums):
    if isinstance(nums, dict):
        nums = nums["nums"]

    largest = 0
    element = nums[0]

    for i in nums:
        count = nums.count(i)

        if count > largest or (count == largest and i < element):
            largest = count
            element = i

    return element
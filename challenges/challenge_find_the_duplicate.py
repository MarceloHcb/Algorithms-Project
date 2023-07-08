def find_duplicate(nums):
    if not nums or isinstance(nums, str):
        return False
    list_num = []
    for n in nums:
        if n in list_num:
            return n
        elif not isinstance(n, int) or n < 1 or n > len(nums) - 1:
            return False
        list_num.append(n)
    return False

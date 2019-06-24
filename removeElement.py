def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return i


if __name__ == '__main__':
    print(removeElement(nums=[3,2,2,3], val=3))
    print(removeElement(nums=[0,1,2,2,3,0,4,2], val=2))
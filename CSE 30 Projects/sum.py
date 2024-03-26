def sum_list(nums):
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    sum = 0
    for num in nums:
        sum += num
    return sum
if __name__ == "__main__":
    listA = []
    listB = [3]
    listC = [1, 2, 3, 4]
    assert sum_list(listA) == None
    assert sum_list(listB) == 3
    assert sum_list(listC) == 10
    print('Everything works correctly!') 
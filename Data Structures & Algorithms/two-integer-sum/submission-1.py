class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        char_index = {}
        for i in range(len(self.nums)):
            if self.nums[i] not in char_index:
                char_index[self.nums[i]] = [i]
            else:
                char_index[self.nums[i]].append(i)
        for i in range(len(self.nums)):
            rem = self.target - self.nums[i]
            if rem == self.nums[i]:
                if rem in char_index:
                    if len(char_index[rem]) >= 2:
                        return [char_index[rem][0], char_index[rem][1]]
                    else:
                        continue
                else:
                    continue
            else:
                if rem in char_index:
                    return [min(i, char_index[rem][0]), max(i, char_index[rem][0])]
                else:
                    continue
        return [-1, -1]

        
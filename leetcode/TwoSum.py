class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for idx, num in enumerate(nums):
            if num in hashMap:
                hashMap[num].append(idx)
            else:
                hashMap[num] = [idx]

        for x in nums:
            y = target - x
            if y == x and len(hashMap[y]) == 2:
                ans = hashMap[y]
                break
            if y != x:
                if y in hashMap:
                    ans = [hashMap[x][0], hashMap[y][0]]
                    break

        return sorted(ans)

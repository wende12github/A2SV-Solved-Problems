class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        result = 0
        skill.sort()
        left = 0
        right = n-1

        while left < right:
            _sum = skill[left] + skill[right]
            sum1 = skill[left + 1] + skill[right - 1]
            if _sum == sum1:
                result += skill[left]*skill[right]
            else:
                return -1
            left += 1
            right -= 1
        return result

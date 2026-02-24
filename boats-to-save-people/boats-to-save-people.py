class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left , right = 0, len(people)-1
        result = 0

        while left <= right:
            current = people[left] + people[right]
            if left == right:
                result += 1
                break

            if current > limit:
                result += 1
                right -= 1
            else:
                left += 1
                right -= 1
                result += 1

        return result

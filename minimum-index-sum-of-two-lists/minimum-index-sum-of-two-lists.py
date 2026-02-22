class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = []
        min_index = float('inf')

        for i in range(len(list1)):
            if list1[i] in list2:
                _index = list2.index(list1[i])
                index_sum = i + _index

                if index_sum < min_index:
                    min_index = index_sum
                    result = [list1[i]]
                    
                elif index_sum == min_index:
                    result.append(list1[i])

        return result

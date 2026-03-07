class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dicts={}
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i + j not in dicts:
                    dicts[i+j] = [mat[i][j]]
                else:
                    dicts[i+j].append(mat[i][j])
        result= []
        for diagonal in dicts.items():
            if diagonal[0] % 2 == 0:
                [result.append(x) for x in diagonal[1][::-1]]
            else:
                [result.append(x) for x in diagonal[1]]
        return result
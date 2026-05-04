class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        indx_1, indx_2 = 0, 0
        n1, n2 = len(version1), len(version2)

        while indx_1 < n1 or indx_2 < n2:
            v1 = v2 = 0
            while indx_1 < n1 and version1[indx_1] != '.':
                v1 = v1 * 10 + (ord(version1[indx_1]) - ord('0'))
                indx_1 += 1

            while indx_2 < n2 and version2[indx_2] != '.':
                v2 = v2 * 10 + (ord(version2[indx_2]) - ord('0'))
                indx_2 += 1

            if v1 < v2:
                return -1
            if v1 > v2:
                return 1
                
            indx_1 += 1
            indx_2 += 1
        return 0
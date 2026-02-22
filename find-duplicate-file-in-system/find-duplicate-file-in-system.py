class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_tapl = defaultdict(list)

        for path in paths:
            path = path.split(" ")
            folder = path[0]

            for _str in path[1:]:
                _str = _str.split(".txt")
                name = _str[0]
                content = _str[1]
                content_tapl[content].append((folder, name))

        result_out = []
        for key, value in content_tapl.items():
            if len(value) > 1:
                temp = []
                
                for path, name in value:
                    temp.append(path + '/' + name + '.txt')
                result_out.append(temp)

        return result_out

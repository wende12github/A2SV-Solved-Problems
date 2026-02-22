class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        temp_buffer = []
        in_block_comment = False

        for line_str in source:
            i = 0
            while i < len(line_str):
                if not in_block_comment:
                    if i + 1 < len(line_str) and line_str[i:i+2] == "/*":
                        in_block_comment = True
                        i += 2
                    elif i + 1 < len(line_str) and line_str[i:i+2] == "//":
                        break
                    else:
                        temp_buffer.append(line_str[i])
                        i += 1
                else:
                    if i + 1 < len(line_str) and line_str[i:i+2] == "*/":
                        in_block_comment = False
                        i += 2
                    else:
                        i += 1
            if not in_block_comment and temp_buffer:
                result.append("".join(temp_buffer))
                temp_buffer = []

        return result

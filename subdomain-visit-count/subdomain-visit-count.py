class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        content = Counter()

        for cpdo in cpdomains:
            num, _str = cpdo.split()
            content[_str] += int(num)
            
            for i in range(len(_str)):
                if _str[i] == ".":
                    content[_str[i+1:]] += int(num)

        return [" ".join((str(v), k)) for k, v in content.items()]

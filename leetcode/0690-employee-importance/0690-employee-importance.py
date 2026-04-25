"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        queue = deque()
        emp = {e.id: e for e in employees}
        queue.append(id)

        result = 0
        while queue:
            emp_id = queue.popleft()
            empl = emp[emp_id]

            for em in empl.subordinates:
                queue.append(em)
            result += empl.importance

        return result
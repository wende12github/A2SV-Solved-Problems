class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        new_g = m
        for i in range(n):
            if group[i] == -1:
                group[i] = new_g
                new_g += 1
        
        group_items = defaultdict(list)
        item_graph = defaultdict(list)
        item_in_degree = defaultdict(int)
        
        group_graph = defaultdict(list)
        group_in_degree = defaultdict(int)
        
        for i in range(n):
            group_items[group[i]].append(i)
            for before in beforeItems[i]:
                if group[i] == group[before]:
                    item_graph[before].append(i)
                    item_in_degree[i] += 1
                else:
                    group_graph[group[before]].append(group[i])
                    group_in_degree[group[i]] += 1

        def topoSort(nodes, graph, in_degree):
            queue = deque([node for node in nodes if in_degree[node] == 0])

            result = []
            while queue:
                u = queue.popleft()
                result.append(u)

                for v in graph[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)

            return result if len(result) == len(nodes) else []

        group_ids = list(group_items.keys())
        groups_order = topoSort(group_ids, group_graph, group_in_degree)

        if not groups_order:
            return []

        result = []
        for g_id in groups_order:
            items = group_items[g_id]
            sorted_items = topoSort(items, item_graph, item_in_degree)

            if not sorted_items:
                return []
                
            result.extend(sorted_items)
            
        return result
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        def dfs(node):  # (bottom up)
            if node in visited:
                return 
            
            # mark as seen
            visited.add(node)
            
            # recur to neghibours
            for neigh in adjs[node]:
                # skip; seen before
                if neigh in visited:
                    continue 
                
                # recur on neigh 
                dfs(neigh)

                # update node xor scores for node
                prefix[node] ^= prefix[neigh]

                # update parent and children relationship
                children[node].add(neigh)

                # remove overlaps 
                children[node] |= children[neigh]
                
        n = len(nums)

        # indegree[i] := degree of the ith node
        indegree = [0] * n

        # 1. build adjacency list of the graph
        adjs = defaultdict(list)
        for src, des in edges:
            adjs[src] += [des]
            adjs[des] += [src]
            indegree[src] += 1
            indegree[des] += 1
        
        # 2. get the max_degree
        max_degree = max(indegree)

        # 3. set the root the node with maximum degree
        for i, degree in enumerate(indegree):
            if degree == max_degree: 
                root = i

        # prefix[i] := xor score of the ith node starting at root node
        prefix = [num for num in nums]   
        visited = set()                   # track down the visited nodes in the graph    
        children = defaultdict(set)       # stores {parent: set of all the children nodes}

        # 4. run dfs starting at root
        dfs(root)

        res = float('inf')

        # 5. pick every pair of 2 edges 
        for i in range(1, n - 1):
            for j in range(i):
                (a, b), (c, d) = edges[i], edges[j]

                # swap if b is the child; (a, b) = (child, parent)
                if b in children[a]: 
                    a, b = b, a

                # swap if d is the child; (c, d) = (child, parent)
                if d in children[c]: 
                    c, d = d, c

                # compare (a, c) as the children 

                # case1; c is a child of a
                if c in children[a]: 
                    part1 = prefix[c]                   # c is the root of part1
                    part2 = prefix[a] ^ prefix[c]       # remove c from a
                    part3 = prefix[root] ^ prefix[a]    # remove a from root

                # case2; a is a child of c
                elif a in children[c]: 
                    part1 = prefix[a]                   # a is the root of part1
                    part2 = prefix[c] ^ prefix[a]       # remove a from c
                    part3 = prefix[root] ^ prefix[c]    # remove c from root

                # case3; no relationship between a & c
                else: 
                    part1 = prefix[a]                   # a is the root of part1
                    part2 = prefix[c]                   # c is the root of part2
                    part3 = prefix[root] ^ prefix[a] ^ prefix[c]    # remove a & c from root
                # update res
                delta = max(part1, part2, part3) - min(part1, part2, part3)
                res = min(res, delta)

        return res
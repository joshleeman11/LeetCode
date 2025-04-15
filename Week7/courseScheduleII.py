from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses
        queue = deque([])
        order = []

        for pre in prerequisites:
            [course, prereq] = pre
            graph[prereq].append(course)
            inDegree[course] += 1

        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)


        while queue:
            course = queue.popleft()
            order.append(course)

            for nextCourse in graph[course]:
                inDegree[nextCourse] -= 1
                if inDegree[nextCourse] == 0:
                    queue.append(nextCourse)

        if len(order) != numCourses:
            return []
        return order